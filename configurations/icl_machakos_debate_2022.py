from core_data_modules.cleaners import swahili

from src.pipeline_configuration_spec import *

PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="icl_machakos_debate_2022",
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
                    FlowResultConfiguration("icl_machakos_demog_2022", "ward", "location"),
                    FlowResultConfiguration("icl_machakos_demog_2022", "gender", "gender"),
                    FlowResultConfiguration("icl_machakos_demog_2022", "age", "age"),

                    FlowResultConfiguration("icl_machakos_county_priorities_activation_2022",
                                            "machakos_county_priorities_2022", "machakos_county_priorities_2022"),
                    FlowResultConfiguration("icl_machakos_womenrep_poll_activation_2022",
                                            "machakos_womenrep_poll_2022", "machakos_womenrep_poll_2022"),
                    FlowResultConfiguration("icl_machakos_senator_poll_activation_2022", "machakos_senator_poll_2022",
                                            "machakos_senator_poll_2022"),
                    FlowResultConfiguration("icl_machakos_governor_poll_activation_2022", "machakos_governor_poll_2022",
                                            "machakos_governor_poll_2022")
                ],
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
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/kenya_constituency"), auto_coder=None),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/kenya_county"), auto_coder=None)
                    ],
                    ws_code_string_value="location"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_gender",
                    engagement_db_dataset="gender",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/gender"),
                                                auto_coder=swahili.DemographicCleaner.clean_gender)
                    ],
                    ws_code_string_value="gender"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_age",
                    engagement_db_dataset="age",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/age"), auto_coder=lambda x:
                                                str(swahili.DemographicCleaner.clean_age_within_range(x)))
                    ],
                    ws_code_string_value="age"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_disabled",
                    engagement_db_dataset="disabled",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/disabled"), auto_coder=None)
                    ],
                    ws_code_string_value="disabled"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_old_rqa_datasets",
                    engagement_db_dataset="kenya_pool_old_rqa_datasets",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("kenya_pool_old_rqa_datasets"), auto_coder=None)
                    ],
                    ws_code_string_value="kenya_pool_old_rqa_datasets"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_county_priorities_2022",
                    engagement_db_dataset="machakos_county_priorities_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_county_priorities_2022"),
                                                auto_coder=None),
                    ],
                    ws_code_string_value="icl_machakos_county_priorities_2022"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_womenrep_poll_2022",
                    engagement_db_dataset="machakos_womenrep_poll_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_womenrep_poll_2022"),
                                                auto_coder=None),
                    ],
                    ws_code_string_value="icl_machakos_womenrep_poll_2022"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_senator_poll_2022",
                    engagement_db_dataset="machakos_senator_poll_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_senator_poll_2022"),
                                                auto_coder=None),
                    ],
                    ws_code_string_value="icl_machakos_senator_poll_2022"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_governor_poll_2022",
                    engagement_db_dataset="machakos_governor_poll_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_governor_poll_2022"),
                                                auto_coder=None),
                    ],
                    ws_code_string_value="icl_machakos_governor_poll_2022"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2022/POOL-KENYA/pool-kenya-users.json",
            default_ws_dataset="kenya_pool_old_rqa_datasets"
        )
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2022/ICL/"
    )
)
