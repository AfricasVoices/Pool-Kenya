from core_data_modules.cleaners import swahili
from dateutil.parser import isoparse
from src.pipeline_configuration_spec import *

PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="SDC_GAU",
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
                token_file_url="gs://avf-credentials/pool-kenya-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    # FlowResultConfiguration("sdc_gau_s01_demog", "pool_kenya_location", "location"),
                    # FlowResultConfiguration("sdc_gau_s01_demog", "pool_kenya_gender", "gender"),
                    # FlowResultConfiguration("sdc_gau_s01_demog", "pool_kenya_age", "age"),
                    # FlowResultConfiguration("sdc_gau_s01_demog", "pool_kenya_disabled", "disabled"),
                    # FlowResultConfiguration("sdc_gau_s01_demog", "preferred_language", "preferred_language"),

                    # FlowResultConfiguration("sdc_gau_s01e01_activation", "rqa_s01e01", "sdc_gau_s01e01"),
                    # FlowResultConfiguration("sdc_gau_s01e02_activation", "rqa_s01e02", "sdc_gau_s01e02"),
                    # FlowResultConfiguration("sdc_gau_s01e03_activation", "rqa_s01e03", "sdc_gau_s01e03"),
                    FlowResultConfiguration("sdc_gau_s01e04_activation", "rqa_s01e04", "sdc_gau_s01e04"),
                    # FlowResultConfiguration("sdc_gau_s01e05_activation", "rqa_s01e05", "sdc_gau_s01e05"),
                    # FlowResultConfiguration("sdc_gau_s01e06_activation", "rqa_s01e06", "sdc_gau_s01e06"),
                    # FlowResultConfiguration("sdc_gau_s01e07_activation", "rqa_s01e07", "sdc_gau_s01e07"),

                    # FlowResultConfiguration("sdc_gau_s01e01_follow_up_activation", "rqa_s01e01_follow_up", "sdc_gau_s01e01_follow_up"),
                    # FlowResultConfiguration("sdc_gau_s01e03_follow_up_activation", "rqa_s01e03_follow_up", "sdc_gau_s01e03_follow_up"),
                    # FlowResultConfiguration("sdc_gau_s01e04_follow_up_activation", "rqa_s01e04_follow_up", "sdc_gau_s01e04_follow_up"),
                    # FlowResultConfiguration("sdc_gau_s01e06_follow_up_activation", "rqa_s01e06_follow_up", "sdc_gau_s01e06_follow_up"),
                    # FlowResultConfiguration("sdc_gau_s01e07_follow_up_activation", "rqa_s01e07_follow_up", "sdc_gau_s01e07_follow_up")
                ],
            )
        )
    ],
    coda_sync=CodaConfiguration(
        coda=CodaClientConfiguration(credentials_file_url="gs://avf-credentials/coda-production.json"),
        sync_config=CodaSyncConfiguration(
            dataset_configurations=[
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e01",
                    engagement_db_dataset="sdc_gau_s01e01",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e01"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e01"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e02",
                    engagement_db_dataset="sdc_gau_s01e02",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e02"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e02"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e03",
                    engagement_db_dataset="sdc_gau_s01e03",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e03"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e03"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e04",
                    engagement_db_dataset="sdc_gau_s01e04",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e04"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e04"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e05",
                    engagement_db_dataset="sdc_gau_s01e05",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e05"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e05"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e06",
                    engagement_db_dataset="sdc_gau_s01e06",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e06"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e06"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e07",
                    engagement_db_dataset="sdc_gau_s01e07",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e07"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e07"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e01_follow_up",
                    engagement_db_dataset="sdc_gau_s01e01_follow_up",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e01_follow_up"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e01_follow_up"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e03_follow_up",
                    engagement_db_dataset="sdc_gau_s01e03_follow_up",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e03_follow_up"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e03_follow_up"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e04_follow_up",
                    engagement_db_dataset="sdc_gau_s01e04_follow_up",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e04_follow_up"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e04_follow_up"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e06_follow_up",
                    engagement_db_dataset="sdc_gau_s01e06_follow_up",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e06_follow_up"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e06_follow_up"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_GAU_s01e07_follow_up",
                    engagement_db_dataset="sdc_gau_s01e07_follow_up",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e07_follow_up"), 
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="sdc_gau_s01e07_follow_up"
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
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2022/POOL-KENYA/pool-kenya-users.json",
            default_ws_dataset="kenya_pool_old_rqa_datasets"
        )
    ),
    analysis=AnalysisConfiguration(
        #Temporarily disabled due to drive issues
        # google_drive_upload=GoogleDriveUploadConfiguration(
        #     credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json",
        #     drive_dir="sdc_gau_analysis_output"
        # ),
        dataset_configurations=[
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_gau_s01e01"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_gau_s01e01_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e01"),
                        analysis_dataset="s01e01"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_gau_s01e02"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_gau_s01e02_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e02"),
                        analysis_dataset="s01e02"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_gau_s01e03"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_gau_s01e03_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e03"),
                        analysis_dataset="s01e03"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_gau_s01e04"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_gau_s01e04_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e04"),
                        analysis_dataset="s01e04"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_gau_s01e05"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_gau_s01e05_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e05"),
                        analysis_dataset="s01e05"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_gau_s01e06"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_gau_s01e06_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e06"),
                        analysis_dataset="s01e06"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_gau_s01e07"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_gau_s01e07_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e07"),
                        analysis_dataset="s01e07"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_gau_s01e01_follow_up"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_gau_s01e01_follow_up_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_gau/sdc_gau_s01e01_follow_up"),
                        analysis_dataset="s01e01 follow-up"
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
        traffic_labels=[
            TrafficLabel(label="s01e03 Promos", start_date=isoparse("2023-09-15T16:00+03:00"), end_date=isoparse("2023-08-18T17:00+03:00")),
            TrafficLabel(label="s01e03 SMS Ad", start_date=isoparse("2023-08-18T17:00+03:00"), end_date=isoparse("2023-08-18T20:00+03:00")),
            TrafficLabel(label="s01e03 EJOK & STAR FM", start_date=isoparse("2023-08-18T20:00+03:00"), end_date=isoparse("2023-08-18T22:00+03:00")),
            TrafficLabel(label="s01e03 ANGAF FM", start_date=isoparse("2023-08-19T16:30+03:00"), end_date=isoparse("2023-08-19T18:30+03:00")),
            TrafficLabel(label="s01e03 NORTHRIFT FM", start_date=isoparse("2023-08-19T20:00+03:00"), end_date=isoparse("2023-08-19T22:00+03:00")),
            TrafficLabel(label="s01e03 ASHE & IBSE FM", start_date=isoparse("2023-08-20T20:00+03:00"), end_date=isoparse("2023-08-20T22:00+03:00")),
            TrafficLabel(label="s01e03 PWANI FM", start_date=isoparse("2023-08-20T08:00+03:00"), end_date=isoparse("2023-08-20T10:00+03:00")),

            TrafficLabel(label="s01e04 Promos", start_date=isoparse("2023-09-22T16:00+03:00"), end_date=isoparse("2023-08-25T17:00+03:00")),
            TrafficLabel(label="s01e04 SMS Ad", start_date=isoparse("2023-08-25T17:00+03:00"), end_date=isoparse("2023-08-25T20:00+03:00")),
            TrafficLabel(label="s01e04 EJOK & STAR FM", start_date=isoparse("2023-08-25T20:00+03:00"), end_date=isoparse("2023-08-25T22:00+03:00")),
            TrafficLabel(label="s01e04 ANGAF FM", start_date=isoparse("2023-08-26T16:30+03:00"), end_date=isoparse("2023-08-26T18:30+03:00")),
            TrafficLabel(label="s01e04 NORTHRIFT FM", start_date=isoparse("2023-08-26T20:00+03:00"), end_date=isoparse("2023-08-26T22:00+03:00")),
            TrafficLabel(label="s01e04 PWANI FM", start_date=isoparse("2023-08-27T08:00+03:00"), end_date=isoparse("2023-08-27T10:00+03:00")),
            TrafficLabel(label="s01e04 ASHE & IBSE FM", start_date=isoparse("2023-08-27T20:00+03:00"), end_date=isoparse("2023-08-27T22:00+03:00")),
            
            TrafficLabel(label="s01e05 Promos", start_date=isoparse("2023-09-02T16:00+03:00"), end_date=isoparse("2023-09-02T17:00+03:00")),
            TrafficLabel(label="s01e05 SMS Ad", start_date=isoparse("2023-09-02T17:00+03:00"), end_date=isoparse("2023-09-02T20:00+03:00")),
            TrafficLabel(label="s01e05 EJOK & STAR FM", start_date=isoparse("2023-09-02T20:00+03:00"), end_date=isoparse("2023-09-02T22:00+03:00")),
            TrafficLabel(label="s01e05 ANGAF FM", start_date=isoparse("2023-09-03T16:30+03:00"), end_date=isoparse("2023-09-03T18:30+03:00")),
            TrafficLabel(label="s01e05 NORTHRIFT FM", start_date=isoparse("2023-09-03T20:00+03:00"), end_date=isoparse("2023-09-03T22:00+03:00")),
            TrafficLabel(label="s01e05 PWANI FM", start_date=isoparse("2023-09-04T08:00+03:00"), end_date=isoparse("2023-09-04T10:00+03:00")),
            TrafficLabel(label="s01e05 ASHE & IBSE FM", start_date=isoparse("2023-09-04T20:00+03:00"), end_date=isoparse("2023-09-04T22:00+03:00")),

            TrafficLabel(label="s01e06 Promos", start_date=isoparse("2023-09-06T16:00+03:00"), end_date=isoparse("2023-09-09T17:00+03:00")),
            TrafficLabel(label="s01e06 SMS Ad", start_date=isoparse("2023-09-09T17:00+03:00"), end_date=isoparse("2023-09-09T20:00+03:00")),
            TrafficLabel(label="s01e06 EJOK & STAR FM", start_date=isoparse("2023-09-09T20:00+03:00"), end_date=isoparse("2023-09-09T22:00+03:00")),
            TrafficLabel(label="s01e06 ANGAF FM", start_date=isoparse("2023-09-10T16:30+03:00"), end_date=isoparse("2023-09-10T18:30+03:00")),
            TrafficLabel(label="s01e06 NORTHRIFT FM", start_date=isoparse("2023-09-10T20:00+03:00"), end_date=isoparse("2023-09-10T22:00+03:00")),
            TrafficLabel(label="s01e06 PWANI FM", start_date=isoparse("2023-09-11T08:00+03:00"), end_date=isoparse("2023-09-11T10:00+03:00")),
            TrafficLabel(label="s01e06 ASHE & IBSE FM", start_date=isoparse("2023-09-11T20:00+03:00"), end_date=isoparse("2023-09-11T22:00+03:00")),

            TrafficLabel(label="s01e07 Promos", start_date=isoparse("2023-09-13T16:00+03:00"), end_date=isoparse("2023-09-16T17:00+03:00")),
            TrafficLabel(label="s01e07 SMS Ad", start_date=isoparse("2023-09-16T17:00+03:00"), end_date=isoparse("2023-09-16T20:00+03:00")),
            TrafficLabel(label="s01e07 EJOK & STAR FM", start_date=isoparse("2023-09-16T20:00+03:00"), end_date=isoparse("2023-09-16T22:00+03:00")),
            TrafficLabel(label="s01e07 ANGAF FM", start_date=isoparse("2023-09-17T16:30+03:00"), end_date=isoparse("2023-09-17T18:30+03:00")),
            TrafficLabel(label="s01e07 NORTHRIFT FM", start_date=isoparse("2023-09-17T20:00+03:00"), end_date=isoparse("2023-09-17T22:00+03:00")),
            TrafficLabel(label="s01e07 PWANI FM", start_date=isoparse("2023-09-18T08:00+03:00"), end_date=isoparse("2023-09-18T10:00+03:00")),
            TrafficLabel(label="s01e07 ASHE & IBSE FM", start_date=isoparse("2023-09-18T20:00+03:00"), end_date=isoparse("2023-09-18T22:00+03:00"))
        ]
    ),
    rapid_pro_target=RapidProTarget(
        rapid_pro=RapidProClientConfiguration(
            domain="textit.com",
            token_file_url="gs://avf-credentials/pool-kenya-textit-token.txt"
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
                engagement_db_datasets=["age", "gender", "location", "disabled", "preferred_language", "sdc_gau_s01e01", "sdc_gau_s01e02", 
                                        "sdc_gau_s01e03", "sdc_gau_s01e04", "sdc_gau_s01e05", "sdc_gau_s01e06", "sdc_gau_s01e07", "Ssdc_gau_s01e03_follow_up", 
                                        "sdc_gau_s01e04_follow_up", "sdc_gau_s01e05_follow_up", "sdc_gau_s01e06_follow_up", "sdc_gau_s01e07_follow_up"],
                rapid_pro_contact_field=ContactField(key="pool_kenya_consent_withdrawn", label="pool kenya consent withdrawn")
            ),
            write_mode=WriteModes.CONCATENATE_TEXTS,
            allow_clearing_fields=False,
            weekly_advert_contact_field=ContactField(key="sdc_gau_pool_advert_contact",
                                                     label="sdc gau pool advert contact"),
            sync_advert_contacts=False,
        )     
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2023/SDC_GAU/"
    )
)