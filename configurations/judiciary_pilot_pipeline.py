from core_data_modules.cleaners import swahili
from dateutil.parser import isoparse
from src.pipeline_configuration_spec import *

PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="Global Fund",
    test_participant_uuids=[],
    engagement_database=EngagementDatabaseClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-engagement-databases-firebase-credentials-file.json",
        database_path="engagement_databases/POOL-KENYA"
    ),
    uuid_table=UUIDTableClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-id-infrastructure-firebase-adminsdk-6xps8-b9173f2bfd.json",
        table_name="avf-global-urn-to-participant-uuid",
        uuid_prefix="avf-participant-uuid-"
    ),
    operations_dashboard=OperationsDashboardConfiguration(
        credentials_file_url="gs://avf-credentials/avf-dashboards-firebase-adminsdk-gvecb-ef772e79b6.json",
    ),
    google_form_sources=[
        GoogleFormSource(
            google_form_client=GoogleFormsClientConfiguration(
                credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json"
            ),
            sync_config=GoogleFormToEngagementDBConfiguration(
                form_id="16SywNx3MoXuFEF0bQEpJuZhIMYrbT5y0FqcmpJ-keB4",
                question_configurations=[
                    # RQAs
                    QuestionConfiguration(question_ids=["07080f07"], engagement_db_dataset="sdc_cc_eval_1_lessons_learned"),
                    QuestionConfiguration(question_ids=["313fbefb"], engagement_db_dataset="sdc_cc_eval_2_decision_making"),
                    QuestionConfiguration(question_ids=["3c7de91e"], engagement_db_dataset="sdc_cc_eval_3_suggestions"),
                    QuestionConfiguration(question_ids=["4a784e12"], engagement_db_dataset="sdc_cc_eval_4_application"),
                    QuestionConfiguration(question_ids=["37bc99c8"], engagement_db_dataset="sdc_cc_eval_5_available_resources"),

                    # Demogs
                    QuestionConfiguration(question_ids=["33d86de1"], engagement_db_dataset="age"),
                    QuestionConfiguration(question_ids=["33ff86fc"], engagement_db_dataset="gender"),
                    QuestionConfiguration(question_ids=["15edfd95"], engagement_db_dataset="household_language"),
                    QuestionConfiguration(question_ids=["265ff47f"], engagement_db_dataset="location"),
                    QuestionConfiguration(question_ids=["1b9b0759"], engagement_db_dataset="recently_displaced"),
                    QuestionConfiguration(question_ids=["353988cc"], engagement_db_dataset="disability"),
                ]
            )
        ),
    ],
    kobotoolbox_sources=[
        KoboToolBoxSource(
            token_file_url="gs://avf-credentials/uraia-kobotoolbox-token.json",
            sync_config=KoboToolBoxToEngagementDBConfiguration(
                asset_uid="aEWQfEwY6MZkGHQyLG2nLw",
                participant_id_configuration=KoboToolBoxParticipantIdConfiguration(
                    data_column_name="group_go9un15/Contacts",
                    id_type=KoboToolBoxParticipantIdTypes.KENYA_MOBILE_NUMBER
                ),
                ignore_invalid_mobile_numbers=True,
                question_configurations=[
                    KoboToolBoxQuestionConfiguration(data_column_name="group_dt2ko10/Gf_s03e01", engagement_db_dataset="gf_s03e01"),
                    KoboToolBoxQuestionConfiguration(data_column_name="group_dt2ko10/Gf_s03e02", engagement_db_dataset="gf_s03e02"),
                    KoboToolBoxQuestionConfiguration(data_column_name="group_dt2ko10/Gf_s03e03", engagement_db_dataset="gf_s03e03"),
                    KoboToolBoxQuestionConfiguration(data_column_name="group_dt2ko10/Gf_s03e04", engagement_db_dataset="gf_s03e04"),

                    KoboToolBoxQuestionConfiguration(data_column_name="group_go9un15/Gender", engagement_db_dataset="gender"),
                    KoboToolBoxQuestionConfiguration(data_column_name="group_go9un15/Age", engagement_db_dataset="age"),
                    KoboToolBoxQuestionConfiguration(data_column_name="group_go9un15/Location", engagement_db_dataset="location"),
                    KoboToolBoxQuestionConfiguration(data_column_name="group_go9un15/Disability", engagement_db_dataset="disabled"),

                    KoboToolBoxQuestionConfiguration(data_column_name="group_tl9vi82/Radio_Show_Participation", engagement_db_dataset="gf_radio_show_participation"),
                    KoboToolBoxQuestionConfiguration(data_column_name="group_tl9vi82/Radio_Show_Participation_001", engagement_db_dataset="gf_radio_show_participation")
                ]
            )
        )
    ],
    coda_sync=CodaConfiguration(
        coda=CodaClientConfiguration(credentials_file_url="gs://avf-credentials/coda-production.json"),
        sync_config=CodaSyncConfiguration(
            dataset_configurations=[
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_location",
                    engagement_db_dataset="location",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/kenya_ward"), auto_coder=None),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/kenya_constituency"), auto_coder=None),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/kenya_county"), auto_coder=None)
                    ],
                    ws_code_match_value="location"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_gender",
                    engagement_db_dataset="gender",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/gender"),
                                                auto_coder=swahili.DemographicCleaner.clean_gender)
                    ],
                    ws_code_match_value="gender"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_age",
                    engagement_db_dataset="age",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/age"), auto_coder=lambda x:
                                                str(swahili.DemographicCleaner.clean_age_within_range(x)))
                    ],
                    ws_code_match_value="age"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_disabled",
                    engagement_db_dataset="disabled",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/disabled"), auto_coder=None)
                    ],
                    ws_code_match_value="disabled"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_preferred_language",
                    engagement_db_dataset="preferred_language",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/preferred_language"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="preferred_language"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2022/POOL-KENYA/pool-kenya-users.json",
            default_ws_dataset="kenya_pool_old_rqa_datasets"
        )
    ),
    analysis=AnalysisConfiguration(
        google_drive_upload=GoogleDriveUploadConfiguration(
            credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json",
            drive_dir="global_fund_s03_analysis_output"
        ),
        dataset_configurations=[
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["preferred_language"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="preferred_language_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/preferred_language"),
                        analysis_dataset="preferred_language"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["gender"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="gender_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/gender"),
                        analysis_dataset="gender"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["disabled"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="disabled_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/disabled"),
                        analysis_dataset="disabled"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                 engagement_db_datasets=["location"],
                 dataset_type=DatasetTypes.DEMOGRAPHIC,
                 raw_dataset="location_raw",
                 coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/kenya_county"),
                        analysis_dataset="kenya_county",
                        analysis_location=AnalysisLocations.KENYA_COUNTY
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/kenya_constituency"),
                        analysis_dataset="kenya_constituency",
                        analysis_location=AnalysisLocations.KENYA_CONSTITUENCY
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/kenya_ward"),
                        analysis_dataset="kenya_ward",
                        analysis_location=AnalysisLocations.KENYA_WARD
                    )
                 ]
             ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["age"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="age_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/age"),
                        analysis_dataset="age"
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/age_category"),
                        analysis_dataset="age_category",
                        age_category_config=AgeCategoryConfiguration(
                            age_analysis_dataset="age",
                            categories={
                                (10, 14): "10 to 14",
                                (15, 17): "15 to 17",
                                (18, 35): "18 to 35",
                                (36, 54): "36 to 54",
                                (55, 99): "55 to 99"
                            }
                        )
                    ),
                ],
            )
        ],
        ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
        maps=[],
        traffic_labels=[]
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2024/judiciary_pilot/"
    )
)
