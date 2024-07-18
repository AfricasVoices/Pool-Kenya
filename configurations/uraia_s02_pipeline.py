from core_data_modules.cleaners import swahili
from dateutil.parser import isoparse
from src.pipeline_configuration_spec import *

PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="Uraia",
    test_participant_uuids=[
        "avf-participant-uuid-ced0f78f-f989-42e4-8813-b1ead4fff0ae",
        "avf-participant-uuid-d38dcb19-5170-4441-99de-5aa3e9bcafc1",
        "avf-participant-uuid-2fa53f8c-8f71-490c-8aff-40c6929b2675", 
        "avf-participant-uuid-7d817591-37b9-43ef-b3c3-303fdfa1544f", 
        "avf-participant-uuid-f24811c3-90a6-4fcd-bf32-e8b38eb98ca4", 
        "avf-participant-uuid-9fe96ca0-18ba-474c-b86f-c4709f45d4ca", 
        "avf-participant-uuid-dbc84ba4-f55f-4741-b1c8-7b87727f19e1", 
        "avf-participant-uuid-b972d5f2-be30-4eea-be1c-a4d973a15330", 
        "avf-participant-uuid-73b4f00a-5e49-418d-896f-95185f59fe4d", 
        "avf-participant-uuid-7d144e9e-b54f-4d1f-bca9-3e8cdeeaedcc", 
        "avf-participant-uuid-88ef05ba-4c56-41f8-a00c-29104abab73e", 
        "avf-participant-uuid-5ca68e07-3dba-484b-a29c-7a6c989036b7"
    ],
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
    rapid_pro_sources=[
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/pool-kenya-2-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("uraia_s01_demogs", "pool_kenya_location", "location"),
                    FlowResultConfiguration("uraia_s01_demogs", "pool_kenya_gender", "gender"),
                    FlowResultConfiguration("uraia_s01_demogs", "pool_kenya_age", "age"),
                    FlowResultConfiguration("uraia_s01_demogs", "pool_kenya_disabled", "disabled"),
                    FlowResultConfiguration("uraia_s01_demogs", "preferred_language", "preferred_language"),

                    FlowResultConfiguration("uraia_s02_evaluation", "uraia_political_agency", "uraia_political_agency"),
                    FlowResultConfiguration("uraia_s02_evaluation", "uraia_personal_initiatives", "uraia_personal_initiatives"),
                    FlowResultConfiguration("uraia_s02_evaluation", "uraia_climate_change_understanding", "uraia_climate_change_understanding"),

                    FlowResultConfiguration("uraia_s02e01_activation", "rqa_s02e01", "uraia_s02e01"),
                    FlowResultConfiguration("uraia_s02e02_activation", "rqa_s02e02", "uraia_s02e02"),
                    FlowResultConfiguration("uraia_s02e03_activation", "rqa_s02e03", "uraia_s02e03"),
                    FlowResultConfiguration("uraia_s02e04_activation", "rqa_s02e04", "uraia_s02e04")
                ],
            )
        )
    ],
    kobotoolbox_sources=[
        KoboToolBoxSource(
            token_file_url="gs://avf-credentials/uraia-kobotoolbox-token.json",
            sync_config=KoboToolBoxToEngagementDBConfiguration(
                asset_uid="aAarneBJYgfBEUzQoATwKW",
                participant_id_configuration=KoboToolBoxParticipantIdConfiguration(
                    data_column_name="Contacts",
                    id_type=KoboToolBoxParticipantIdTypes.KENYA_MOBILE_NUMBER
                ),
                ignore_invalid_mobile_numbers=True,
                question_configurations=[
                    KoboToolBoxQuestionConfiguration(data_column_name="uraia_e01", engagement_db_dataset="uraia_s02e01"),
                    KoboToolBoxQuestionConfiguration(data_column_name="uraia_e02", engagement_db_dataset="uraia_s02e02"),

                    KoboToolBoxQuestionConfiguration(data_column_name="Gender", engagement_db_dataset="gender"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Age", engagement_db_dataset="age"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Ward", engagement_db_dataset="location"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Disability", engagement_db_dataset="disabled"),

                    KoboToolBoxQuestionConfiguration(data_column_name="Radio_Access", engagement_db_dataset="uraia_radio_access"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Mobile_Phone_Access", engagement_db_dataset="uraia_mobile_phone_access"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Radio_Topic", engagement_db_dataset="uraia_radio_topic"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Radio_Topic_001", engagement_db_dataset="uraia_radio_topic_reason"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Literacy", engagement_db_dataset="uraia_literacy"),
                ]
            )
        ),
        KoboToolBoxSource(
            token_file_url="gs://avf-credentials/uraia-kobotoolbox-token.json",
            sync_config=KoboToolBoxToEngagementDBConfiguration(
                asset_uid="a4jEmfaFMnHALwfTGTRRBX",
                participant_id_configuration=KoboToolBoxParticipantIdConfiguration(
                    data_column_name="Contacts",
                    id_type=KoboToolBoxParticipantIdTypes.KENYA_MOBILE_NUMBER
                ),
                ignore_invalid_mobile_numbers=True,
                question_configurations=[
                    KoboToolBoxQuestionConfiguration(data_column_name="uraia_s02e03", engagement_db_dataset="uraia_s02e03"),
                    KoboToolBoxQuestionConfiguration(data_column_name="uraia_s02e04", engagement_db_dataset="uraia_s02e04"),

                    KoboToolBoxQuestionConfiguration(data_column_name="Gender", engagement_db_dataset="gender"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Age", engagement_db_dataset="age"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Ward", engagement_db_dataset="location"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Disability", engagement_db_dataset="disabled"),

                    KoboToolBoxQuestionConfiguration(data_column_name="Radio_Access", engagement_db_dataset="uraia_radio_access"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Mobile_Phone_Access", engagement_db_dataset="uraia_mobile_phone_access"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Radio_Topic", engagement_db_dataset="uraia_radio_topic"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Radio_Topic_001", engagement_db_dataset="uraia_radio_topic_reason"),
                    KoboToolBoxQuestionConfiguration(data_column_name="Literacy", engagement_db_dataset="uraia_literacy"),
                ]
            )
        ),
    ],
    coda_sync=CodaConfiguration(
        coda=CodaClientConfiguration(credentials_file_url="gs://avf-credentials/coda-production.json"),
        sync_config=CodaSyncConfiguration(
            dataset_configurations=[
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_s02e01",
                    engagement_db_dataset="uraia_s02e01",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_s02e01"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_s02e01"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_s02e02",
                    engagement_db_dataset="uraia_s02e02",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_s02e02"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_s02e02"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_s02e03",
                    engagement_db_dataset="uraia_s02e03",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_s02e03"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_s02e03"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_s02e04",
                    engagement_db_dataset="uraia_s02e04",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_s02e04"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_s02e04"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_political_agency",
                    engagement_db_dataset="uraia_political_agency",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_political_agency"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_political_agency"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_personal_initiatives",
                    engagement_db_dataset="uraia_personal_initiatives",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_personal_initiatives"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_personal_initiatives"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_climate_change_understanding",
                    engagement_db_dataset="uraia_climate_change_understanding",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_climate_change_understanding"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_climate_change_understanding"
                ),
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
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_radio_access",
                    engagement_db_dataset="uraia_radio_access",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_radio_access"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_radio_access"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_mobile_phone_access",
                    engagement_db_dataset="uraia_mobile_phone_access",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_mobile_phone_access"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_mobile_phone_access"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_radio_topic",
                    engagement_db_dataset="uraia_radio_topic",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_radio_topic"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_radio_topic"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_radio_topic_reason",
                    engagement_db_dataset="uraia_radio_topic_reason",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_radio_topic_reason"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_radio_topic_reason"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Uraia_literacy",
                    engagement_db_dataset="uraia_literacy",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/uraia/uraia_literacy"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="uraia_literacy"
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
            drive_dir="uraia_s02_analysis_output"
        ),
        dataset_configurations=[
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["uraia_s02e01"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="uraia_s02e01_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/uraia/uraia_s02e01"),
                        analysis_dataset="s02e01"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["uraia_s02e02"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="uraia_s02e02_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/uraia/uraia_s02e02"),
                        analysis_dataset="s02e02"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["uraia_s02e03"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="uraia_s02e03_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/uraia/uraia_s02e03"),
                        analysis_dataset="s02e03"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["uraia_s02e04"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="uraia_s02e04_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/uraia/uraia_s02e04"),
                        analysis_dataset="s02e04"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["uraia_political_agency"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="uraia_political_agency_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/uraia/uraia_political_agency"),
                        analysis_dataset="political_agency"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["uraia_personal_initiatives"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="uraia_personal_initiatives_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/uraia/uraia_personal_initiatives"),
                        analysis_dataset="personal_initiatives"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["uraia_climate_change_understanding"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="uraia_climate_change_understanding_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/uraia/uraia_climate_change_understanding"),
                        analysis_dataset="climate_change_understanding"
                    )
                ],
            ),
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
        traffic_labels=[]
    ),
    rapid_pro_target=RapidProTarget(
        rapid_pro=RapidProClientConfiguration(
            domain="textit.com",
            token_file_url="gs://avf-credentials/pool-kenya-2-textit-token.txt"
        ),
        sync_config=EngagementDBToRapidProConfiguration(
            normal_datasets=[
                DatasetConfiguration(
                    engagement_db_datasets=["age"],
                    rapid_pro_contact_field=ContactField(key="pool_kenya_age", label="pool kenya age")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["gender"],
                    rapid_pro_contact_field=ContactField(key="pool_kenya_gender", label="pool kenya gender")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["location"],
                    rapid_pro_contact_field=ContactField(key="pool_kenya_location", label="pool kenya location")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["disabled"],
                    rapid_pro_contact_field=ContactField(key="pool_kenya_disabled", label="pool kenya disabled")
                ),
            ],
            consent_withdrawn_dataset=DatasetConfiguration(
                engagement_db_datasets=["age", "gender", "location", "disabled", "preferred_language", "uraia_s02e01", "uraia_s02e02",
                                        "uraia_s02e03", "uraia_s02e04", "uraia_political_agency", "uraia_personal_initiatives",
                                        "uraia_climate_change_understanding", "uraia_preferred_contact_mode"],
                rapid_pro_contact_field=ContactField(key="pool_kenya_consent_withdrawn", label="pool kenya consent withdrawn")
            ),
            write_mode=WriteModes.CONCATENATE_TEXTS,
            allow_clearing_fields=False,
            weekly_advert_contact_field=ContactField(key="uraia_pool_advert_contact",
                                                     label="uraia pool advert contact"),
            sync_advert_contacts=False,
        )     
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2023/Uraia/"
    )
)
