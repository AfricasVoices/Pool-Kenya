from core_data_modules.cleaners import swahili

from src.pipeline_configuration_spec import *

PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="AIK-ELECTIONS",
    test_participant_uuids=[
        "avf-participant-uuid-ced0f78f-f989-42e4-8813-b1ead4fff0ae",
        "avf-participant-uuid-2fa53f8c-8f71-490c-8aff-40c6929b2675",
        "avf-participant-uuid-7d817591-37b9-43ef-b3c3-303fdfa1544f",
        "avf-participant-uuid-88ef05ba-4c56-41f8-a00c-29104abab73e",
        "avf-participant-uuid-b972d5f2-be30-4eea-be1c-a4d973a15330",
        "avf-participant-uuid-7d144e9e-b54f-4d1f-bca9-3e8cdeeaedcc",
        "avf-participant-uuid-73b4f00a-5e49-418d-896f-95185f59fe4d",
        "avf-participant-uuid-f24811c3-90a6-4fcd-bf32-e8b38eb98ca4"
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
    # google_form_sources=[
    #     GoogleFormSource(
    #         google_form_client=GoogleFormsClientConfiguration(
    #             credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json"
    #         ),
    #         # TODO: Update google form to engagement db config
    #         sync_config=GoogleFormToEngagementDBConfiguration(
    #             form_id="",
    #             participant_id_configuration=ParticipantIdConfiguration(
    #                 question_title="",
    #                 id_type=""
    #             ),
    #             question_configurations=[]
    #         )
    #     )
    # ],
    rapid_pro_sources=[
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/pool-kenya-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[                   
                    FlowResultConfiguration("AIK_survey_demog", "pool_kenya_age", "age"),
                    FlowResultConfiguration("AIK_survey_demog", "pool_kenya_gender", "gender"),
                    FlowResultConfiguration("AIK_survey_demog", "pool_kenya_location", "location"),
                    FlowResultConfiguration("AIK_survey_demog", "pool_kenya_disabled", "disabled"),

                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_political_participation", "aik_political_participation"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_election_conversations", "aik_election_conversations"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_influence_on_voting_choices", "aik_influence_on_voting_choices"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_concern_about_safety_and_security", "aik_concern_about_safety_and_security"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_incidents_of_violence_and_polarisation", "aik_incidents_of_violence_and_polarisation"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_electoral_sexual_gender_based_violence", "aik_electoral_sexual_gender_based_violence"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_response_to_electoral_related_insecurity", "aik_response_to_electoral_related_insecurity"),
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
                    ws_code_match_value="location",
                    dataset_users_file_url="gs://avf-project-datasets/2022/POOL-KENYA/pool-kenya-users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_gender",
                    engagement_db_dataset="gender",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/gender"),
                                                auto_coder=swahili.DemographicCleaner.clean_gender)
                    ],
                    ws_code_match_value="gender",
                    dataset_users_file_url="gs://avf-project-datasets/2022/POOL-KENYA/pool-kenya-users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_age",
                    engagement_db_dataset="age",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/age"), auto_coder=lambda x:
                                                str(swahili.DemographicCleaner.clean_age_within_range(x)))
                    ],
                    ws_code_match_value="age",
                    dataset_users_file_url="gs://avf-project-datasets/2022/POOL-KENYA/pool-kenya-users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_disabled",
                    engagement_db_dataset="disabled",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/disabled"), auto_coder=None)
                    ],
                    ws_code_match_value="disabled",
                    dataset_users_file_url="gs://avf-project-datasets/2022/POOL-KENYA/pool-kenya-users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_political_participation",
                    engagement_db_dataset="aik_political_participation",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_political_participation"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_political_participation"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_election_conversations",
                    engagement_db_dataset="aik_election_conversations",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_election_conversations"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_election_conversations"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_influence_on_voting_choices",
                    engagement_db_dataset="aik_influence_on_voting_choices",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_influence_on_voting_choices"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_influence_on_voting_choices"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_concern_about_safety_and_security",
                    engagement_db_dataset="aik_concern_about_safety_and_security",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_concern_about_safety_and_security"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_concern_about_safety_and_security"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_incidents_of_violence_and_polarisation",
                    engagement_db_dataset="aik_incidents_of_violence_and_polarisation",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_incidents_of_violence_and_polarisation"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_incidents_of_violence_and_polarisation"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_electoral_sexual_gender_based_violence",
                    engagement_db_dataset="aik_electoral_sexual_gender_based_violence",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_electoral_sexual_gender_based_violence"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_electoral_sexual_gender_based_violence"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_response_to_electoral_related_insecurity",
                    engagement_db_dataset="aik_response_to_electoral_related_insecurity",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_response_to_electoral_related_insecurity"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_response_to_electoral_related_insecurity"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_IEBC_effectiveness",
                    engagement_db_dataset="aik_iebc_effectiveness",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_iebc_effectiveness"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_iebc_effectiveness"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_NPS_effectiveness",
                    engagement_db_dataset="aik_nps_effectiveness",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_nps_effectiveness"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_nps_effectiveness"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_NCIC_effectiveness",
                    engagement_db_dataset="aik_ncic_effectiveness",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_ncic_effectiveness"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_ncic_effectiveness"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_DPP_effectiveness",
                    engagement_db_dataset="aik_dpp_effectiveness",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_dpp_effectiveness"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_dpp_effectiveness"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_IPOA_effectiveness",
                    engagement_db_dataset="aik_ipoa_effectiveness",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_ipoa_effectiveness"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_ipoa_effectiveness"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_judiciary_effectiveness",
                    engagement_db_dataset="aik_judiciary_effectiveness",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_judiciary_effectiveness"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_judiciary_effectiveness"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_KNCHR_effectiveness",
                    engagement_db_dataset="aik_knchr_effectiveness",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_knchr_effectiveness"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_knchr_effectiveness"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_other_institutions_effectiveness",
                    engagement_db_dataset="aik_other_institutions_effectiveness",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_other_institutions_effectiveness"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_other_institutions_effectiveness"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_electoral_violence_anxiety",
                    engagement_db_dataset="aik_electoral_violence_anxiety",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_electoral_violence_anxiety"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_electoral_violence_anxiety"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_hate_speech_and_actions_target",
                    engagement_db_dataset="aik_hate_speech_and_actions_target",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_hate_speech_and_actions_target"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_hate_speech_and_actions_target"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_identity_groups_increase",
                    engagement_db_dataset="aik_identity_groups_increase",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_identity_groups_increase"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_identity_groups_increase"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_inability_to_work",
                    engagement_db_dataset="aik_inability_to_work",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_inability_to_work"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_inability_to_work"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_intolerance_incidents",
                    engagement_db_dataset="aik_intolerance_incidents",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_intolerance_incidents"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_intolerance_incidents"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_peace_and_security_initiatives",
                    engagement_db_dataset="aik_peace_and_security_initiatives",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_peace_and_security_initiatives"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_peace_and_security_initiatives"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_physical_harm",
                    engagement_db_dataset="aik_physical_harm",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_physical_harm"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_physical_harm"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_police_brutality",
                    engagement_db_dataset="aik_police_brutality",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_police_brutality"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_police_brutality"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_political_environment",
                    engagement_db_dataset="aik_political_environment",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_political_environment"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_political_environment"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_political_events_disruption",
                    engagement_db_dataset="aik_political_events_disruption",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_political_events_disruption"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_political_events_disruption"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_sexual_assault",
                    engagement_db_dataset="aik_sexual_assault",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_sexual_assault"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_sexual_assault"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_unsafe_areas",
                    engagement_db_dataset="aik_unsafe_areas",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_unsafe_areas"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_unsafe_areas"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_vandalism_theft_incidents",
                    engagement_db_dataset="aik_vandalism_theft_incidents",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_vandalism_theft_incidents"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_vandalism_theft_incidents"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_violence_displacement",
                    engagement_db_dataset="aik_violence_displacement",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_violence_displacement"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_violence_displacement"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2022/POOL-KENYA/aik_elections_coda_users.json",
        )
    ),
    analysis=AnalysisConfiguration(
        google_drive_upload=GoogleDriveUploadConfiguration(
            credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json",
            drive_dir="aik_elections_analysis_outputs"
        ),
        dataset_configurations=[
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
                        code_scheme=load_code_scheme("demographics/aik_elections_age_category"),
                        analysis_dataset="age_category",
                        age_category_config=AgeCategoryConfiguration(
                            age_analysis_dataset="age",
                            categories={
                                (10, 17): "10 to 17",
                                (18, 24): "18 to 24",
                                (25, 34): "25 to 34",
                                (35, 49): "35 to 49",
                                (50, 64): "50 to 64",
                                (65, 99): "65 to 99"
                            }
                        )
                    ),
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["aik_political_participation"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="aik_political_participation_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/aik/aik_political_participation"),
                        analysis_dataset="aik_political_participation"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["aik_election_conversations"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="aik_election_conversations_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/aik/aik_election_conversations"),
                        analysis_dataset="aik_election_conversations"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["aik_influence_on_voting_choices"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="aik_influence_on_voting_choices_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/aik/aik_influence_on_voting_choices"),
                        analysis_dataset="aik_influence_on_voting_choices"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["aik_concern_about_safety_and_security"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="aik_concern_about_safety_and_security_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/aik/aik_concern_about_safety_and_security"),
                        analysis_dataset="aik_concern_about_safety_and_security"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["aik_incidents_of_violence_and_polarisation"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="aik_incidents_of_violence_and_polarisation_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/aik/aik_incidents_of_violence_and_polarisation"),
                        analysis_dataset="aik_incidents_of_violence_and_polarisation"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["aik_electoral_sexual_gender_based_violence"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="aik_electoral_sexual_gender_based_violence_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/aik/aik_electoral_sexual_gender_based_violence"),
                        analysis_dataset="aik_electoral_sexual_gender_based_violence"
                    )
                ],
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["aik_response_to_electoral_related_insecurity"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="aik_response_to_electoral_related_insecurity_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/aik/aik_response_to_electoral_related_insecurity"),
                        analysis_dataset="aik_response_to_electoral_related_insecurity"
                    )
                ],
            ),
        ],
        ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2022/AIK-ELECTIONS/"
    )
)
