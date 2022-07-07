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
                    FlowResultConfiguration("icl_machakos_poll_registration_activation_2022", "icl_machakos_poll_registration_2022",
                                            "machakos_poll_registration_2022"),
                    FlowResultConfiguration("icl_machakos_demog_2022", "ward", "location"),
                    FlowResultConfiguration("icl_machakos_demog_2022", "gender", "gender"),
                    FlowResultConfiguration("icl_machakos_demog_2022", "age", "age"),

                    FlowResultConfiguration("icl_machakos_county_priorities_activation_2022",
                                            "machakos_county_priorities_2022", "machakos_county_priorities_2022"),
                    FlowResultConfiguration("icl_machakos_womenrep_poll_ad_2022",
                                            "womenrep_poll_2022_selina", "machakos_womenrep_poll_2022"),
                    FlowResultConfiguration("icl_machakos_womenrep_poll_ad_2022_rita",
                                            "womenrep_poll_2022_rita", "machakos_womenrep_poll_2022_rita"),
                    FlowResultConfiguration("icl_machakos_senator_2022_poll_ad", "senator_poll_2022",
                                            "machakos_senator_poll_2022"),
                    FlowResultConfiguration("icl_machakos_governor_poll_ad_2022", "governor_poll_2022",
                                            "machakos_governor_poll_2022"),
                    FlowResultConfiguration("icl_pool_invitation_activation_2022", "icl_pool_invitation_2022",
                                            "icl_pool_invitation_2022")
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
                    coda_dataset_id="Kenya_Pool_old_rqa_datasets",
                    engagement_db_dataset="kenya_pool_old_rqa_datasets",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("kenya_pool_old_rqa_datasets"), auto_coder=None)
                    ],
                    ws_code_match_value="kenya_pool_old_rqa_datasets"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_poll_registration_2022",
                    engagement_db_dataset="machakos_poll_registration_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_poll_registration_2022"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="icl_machakos_poll_registration_2022"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_county_priorities_2022",
                    engagement_db_dataset="machakos_county_priorities_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_county_priorities_2022"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="icl_machakos_county_priorities_2022"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_womenrep_poll_2022",
                    engagement_db_dataset="machakos_womenrep_poll_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_womenrep_poll_2022_selina"),
                                                auto_coder=None),
                    ],
                    ws_code_match_value="icl_machakos_womenrep_poll_2022"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_womenrep_poll_2022_rita",
                    engagement_db_dataset="machakos_womenrep_poll_2022_rita",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_womenrep_poll_2022_rita"),
                                                auto_coder=None),
                    ],
                    ws_code_match_value="icl_machakos_womenrep_poll_2022_rita"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_senator_poll_2022",
                    engagement_db_dataset="machakos_senator_poll_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_senator_poll_2022"),
                                                auto_coder=None),
                    ],
                    ws_code_match_value="icl_machakos_senator_poll_2022"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_machakos_governor_poll_2022",
                    engagement_db_dataset="machakos_governor_poll_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/machakos_governor_poll_2022"),
                                                auto_coder=None),
                    ],
                    ws_code_match_value="icl_machakos_governor_poll_2022"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="ICL_pool_invitation_2022",
                    engagement_db_dataset="icl_pool_invitation_2022",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/icl/icl_pool_invitation_2022"),
                                                auto_coder=None),
                    ],
                    ws_code_match_value="icl_pool_invitation_2022"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2022/POOL-KENYA/pool-kenya-users.json",
            default_ws_dataset="kenya_pool_old_rqa_datasets"
        )
    ),
    analysis=AnalysisConfiguration(
        google_drive_upload=GoogleDriveUploadConfiguration(
            credentials_file_url="gs://avf-credentials/pipeline-runner-2022-service-acct-avf-data-core-64cc71459fe7.json",
            drive_dir="machakos_debate_2022_analysis_outputs"
        ),
        dataset_configurations=[
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["machakos_poll_registration_2022"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="machakos_poll_registration_2022_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/icl/machakos_poll_registration_2022"),
                        analysis_dataset="machakos_poll_registration_2022"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["machakos_county_priorities_2022"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="machakos_county_priorities_2022_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/icl/machakos_county_priorities_2022"),
                        analysis_dataset="machakos_county_priorities_2022"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["machakos_womenrep_poll_2022"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="machakos_womenrep_poll_2022_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/icl/machakos_womenrep_poll_2022_selina"),
                        analysis_dataset="machakos_womenrep_poll_2022"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["machakos_womenrep_poll_2022_rita"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="machakos_womenrep_poll_2022_rita_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/icl/machakos_womenrep_poll_2022_rita"),
                        analysis_dataset="machakos_womenrep_poll_2022_rita"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["machakos_senator_poll_2022"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="machakos_senator_poll_2022_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/icl/machakos_senator_poll_2022"),
                        analysis_dataset="machakos_senator_poll_2022"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["machakos_governor_poll_2022"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="machakos_governor_poll_2022_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/icl/machakos_governor_poll_2022"),
                        analysis_dataset="machakos_governor_poll_2022"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["icl_pool_invitation_2022"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="icl_pool_invitation_2022_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/icl/icl_pool_invitation_2022"),
                        analysis_dataset="icl_pool_invitation_2022"
                    )
                ],
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
                 engagement_db_datasets=["location"],
                 dataset_type=DatasetTypes.DEMOGRAPHIC,
                 raw_dataset="location_raw",
                 coding_configs=[
                     CodingConfiguration(
                         code_scheme=load_code_scheme("demographics/kenya_ward"),
                         analysis_dataset="kenya_ward",
                         analysis_location=AnalysisLocations.KENYA_WARD

                     ),
                     CodingConfiguration(
                         code_scheme=load_code_scheme("demographics/kenya_county"),
                         analysis_dataset="kenya_county",
                         analysis_location=AnalysisLocations.KENYA_COUNTY
                     ),
                     CodingConfiguration(
                         code_scheme=load_code_scheme("demographics/kenya_constituency"),
                         analysis_dataset="kenya_constituency",
                         analysis_location=AnalysisLocations.KENYA_CONSTITUENCY
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
                engagement_db_datasets=["age", "gender", "location", "disabled", "machakos_governor_poll_2022",
                                        "machakos_senator_poll_2022", "machakos_womenrep_poll_2022_rita", "machakos_womenrep_poll_2022",
                                        "machakos_county_priorities_2022", "icl_pool_invitation_2022", "machakos_poll_registration_2022"],
                rapid_pro_contact_field=ContactField(key="pool_kenya_consent_withdrawn", label="pool kenya consent withdrawn")
            ),
            write_mode=WriteModes.CONCATENATE_TEXTS,
            allow_clearing_fields=False,
            weekly_advert_contact_field=ContactField(key="icl_pool_advert_contact",
                                                     label="icl pool advert contact"),
            sync_advert_contacts=True,
        )
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2022/ICL/"
    )
)
