from core_data_modules.cleaners import swahili

from src.pipeline_configuration_spec import *

def make_rqa_analysis_dataset_config(dataset_name, dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER):
    return AnalysisDatasetConfiguration(
        engagement_db_datasets=[dataset_name],
        dataset_type=dataset_type,
        raw_dataset=f"{dataset_name}_raw",
        coding_configs=[
            CodingConfiguration(
                code_scheme=load_code_scheme(f"rqas/aik/{dataset_name}"),
                analysis_dataset=dataset_name
            )
        ]
    )


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
    google_form_sources=[
        GoogleFormSource(
            google_form_client=GoogleFormsClientConfiguration(
                credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json"
            ),
            sync_config=GoogleFormToEngagementDBConfiguration(
                form_id="1zU-4CZRIPCT88qMH352pPMnn_hh_F-j5BWY_vhCPaZ8",
                question_configurations=[
                    # GENERAL ELECTORAL ENVIRONMENT
                    QuestionConfiguration(engagement_db_dataset="aik_voting_participation", question_titles=["Do you plan on voting in the August 9th General Elections?", "Why are you not planning to vote?"]),

                    # PARTICIPATION IN POLITICAL ACTIVITIES
                    QuestionConfiguration(engagement_db_dataset="aik_political_participation", question_titles=["Do you feel comfortable participating in any political activities in your area of residence?", 
                                                                                                               "Give reasons for your answer on political activities participation"]),
                    
                    # HATE SPEECH & INCITEMENT
                    QuestionConfiguration(engagement_db_dataset="aik_election_conversations", question_titles=["In your view, have elections-related conversations become more controversial and conflictual in the past two weeks than the two weeks before? Give details."]),
                    
                    # UNDUE INFLUENCE & CORRUPTION
                    QuestionConfiguration(engagement_db_dataset="aik_influence_on_voting_choices", question_titles=["Based on the campaign activities over the past two weeks, what do you think will influence people's voting choices in your area?"]),

                    # RISKS OF VIOLENCE
                    QuestionConfiguration(engagement_db_dataset="aik_concern_about_safety_and_security", question_titles=["Based on the current political and security environment, are you concerned about safety and security within your community?", "What are you most concerned about?"]),

                    # VIOLENCE INCIDENT
                    QuestionConfiguration(engagement_db_dataset="aik_incidents_of_violence_and_polarisation", question_titles=["Do you know of incidents of violence and polarisation in your community?"]),

                    # ELECTORAL VIOLENCE CONCERN
                    QuestionConfiguration(engagement_db_dataset="aik_electoral_violence_anxiety", question_titles=["Are you or your family/neighbours more worried about electoral violence now than two weeks ago?", 
                                                                                                                  "Why are they worried about electoral violence?"]),

                    # ELECTORAL SEXUAL GENDER-BASED VIOLENCE
                    QuestionConfiguration(engagement_db_dataset="aik_electoral_sexual_gender_based_violence", question_titles=["Are you or your family/neighbours more worried about electoral sexual gender-based violence  now than two weeks ago?", 
                                                                                                                              "Why are they worried about electoral gender-based violence?"]),
                    
                    # INDIVIDUAL AND INSTITUTIONS ROLES IN THIS ELECTION
                    QuestionConfiguration(engagement_db_dataset="aik_response_to_electoral_related_insecurity", question_titles=["How would you respond to electoral related insecurity in your area?\t"]),

                    QuestionConfiguration(engagement_db_dataset="aik_iebc_effectiveness", question_titles=["Independent Electoral and Boundaries Commission (IEBC)"]),
                    QuestionConfiguration(engagement_db_dataset="aik_nps_effectiveness", question_titles=["National Police Service (NPS)"]),
                    QuestionConfiguration(engagement_db_dataset="aik_ncic_effectiveness", question_titles=["National Cohesion and Integration Commission (NCIC)"]),
                    QuestionConfiguration(engagement_db_dataset="aik_dpp_effectiveness", question_titles=["Office of the Director of Public Prosecutions (DPP)"]),
                    QuestionConfiguration(engagement_db_dataset="aik_ipoa_effectiveness", question_titles=["Independent Policing Oversight Authority (IPOA)"]),
                    QuestionConfiguration(engagement_db_dataset="aik_judiciary_effectiveness", question_titles=["The Judiciary"]),
                    QuestionConfiguration(engagement_db_dataset="aik_knchr_effectiveness", question_titles=["Kenya National Commission on Human Rights (KNCHR)"]),
                    QuestionConfiguration(engagement_db_dataset="aik_other_institutions_effectiveness", question_titles=["List other institutions and their ratings?"]),

                    # DEMOGRAPHICS
                    QuestionConfiguration(engagement_db_dataset="pool_kenya_age", question_titles=["How old are you?"]),
                    QuestionConfiguration(engagement_db_dataset="pool_kenya_gender", question_titles=["What is your sex?"]),
                    QuestionConfiguration(engagement_db_dataset="pool_kenya_location", question_titles=["Which constituency do you live in?"]),
                    QuestionConfiguration(engagement_db_dataset="pool_kenya_disabled", question_titles=["Do you have any form of disability?"]),
                ]
            )
        ),
        GoogleFormSource(
            google_form_client=GoogleFormsClientConfiguration(
                credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json"
            ),
            sync_config=GoogleFormToEngagementDBConfiguration(
                form_id="1cEeq9ujJTv381xTXEB0oP0vLNnSLIfP9Rz32zL1HnHk",
                participant_id_configuration=ParticipantIdConfiguration(
                    question_title="What is your phone number",
                    id_type=GoogleFormParticipantIdTypes.KENYA_MOBILE_NUMBER
                ),
                question_configurations=[
                    # Demographic Questions
                    # QuestionConfiguration(engagement_db_dataset="aik_language", question_titles=["We could either do the interview in English or Swahili. Which language would you prefer? "]),
                    QuestionConfiguration(engagement_db_dataset="pool_kenya_age", question_titles=["Do you mind telling me how old you are?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_education", question_titles=["What is the highest level of education attained ? "]),
                    QuestionConfiguration(engagement_db_dataset="aik_employment_status", question_titles=["What is your employment Status ?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_religion", question_titles=["What is your religion ?"]),
                    QuestionConfiguration(engagement_db_dataset="pool_kenya_gender", question_titles=["What is your sex? "]),
                    QuestionConfiguration(engagement_db_dataset="aik_household_income", question_titles=["Approximately what is your gross monthly household income? (I.e. This is the combined monthly income of all your household members). This will help us in determining your social-economic class."]),
                    QuestionConfiguration(engagement_db_dataset="pool_kenya_disabled", question_titles=["Do you have any form of disability? (If disability is visible, do not ask, make the judgement)"]),
                    QuestionConfiguration(engagement_db_dataset="aik_communities", question_titles=["What community do you belong to?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_indigenous_or_minority", question_titles=["Is it considered indigenous or minority?  if yes provide details."]),
                    QuestionConfiguration(engagement_db_dataset="pool_kenya_location", question_titles=["Can I presume that you are currently a resident of; …………… County? [mention name of the target county]", 
                                                                                                       "Can I presume that you are currently a resident of; …………… Sub-County / Constituency? [mention name of the target sub-county]",
                                                                                                       "Can I presume that you are currently a resident of; …………… Ward? [mention name of the target ward]"]),
                    ## GENERAL ELECTORAL ENVIRONMENT
                    QuestionConfiguration(engagement_db_dataset="aik_voting_participation", question_titles=["Do you plan on voting in the August 9th General Elections?", "If NOT, why are you not planning to vote? "]),
                    QuestionConfiguration(engagement_db_dataset="aik_political_participation", question_titles=["Do you feel comfortable participating in any political activities in your area of residence?", 
                                                                                                               "Reasons for your answer on political activities participation."]),
                    QuestionConfiguration(engagement_db_dataset="aik_political_environment", question_titles=["Do you think the political and security environment is conducive to free and fair elections?"]),

                    ## HATE SPEECH AND INCITEMENT 
                    # QuestionConfiguration(engagement_db_dataset="aik_election_conversations", question_titles=["In your view, have elections-related conversations become more controversial and conflictual in the past two weeks than the two weeks before?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_hate_speech_and_actions_target", question_titles=["Have you heard comments or seen actions motivated by hatred/negative attitudes regarding a person's identity in the last two weeks?", 
                                                                                                                      "If YES, What did they target?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_identity_groups_increase", question_titles=["In your view, has there been an increase in groups with strong political identities challenging others with different loyalties?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_political_events_disruption", question_titles=["In your area, has there been an increase in disruption of political events by the opponent's supporters?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_intolerance_incidents", question_titles=["In your area, has there been an increase in bullying, harassment, and general intolerance incidents? ",
                                                                                                             "If YES, on what grounds?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_unsafe_areas", question_titles=["Are there areas in your community that have become more unsafe in the last two weeks?", 
                                                                                                    "If YES, where and why are they unsafe?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_electoral_violence_anxiety", question_titles=["Are you or your family/neighbours more worried about electoral violence than two weeks ago?", 
                                                                                                                  "If YES, why are they worried about electoral violence?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_electoral_sexual_gender_based_violence", question_titles=["Are you or your family/neighbours more worried about electoral gender-based violence than two weeks ago? ", 
                                                                                                                              "If YES, why are they worried about electoral gender-based violence?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_willingness_to_help_victims", question_titles=["Would you be willing to help a neighbour from a different political view or ethnic background if they were attacked?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_engaging_authorities", question_titles=["Does your household know how to safely and quickly report a crime or seek help from the authorities? "]),
                    QuestionConfiguration(engagement_db_dataset="aik_incitement_sources", question_titles=["Which sources have you seen or heard hateful/inciteful statements about other communities, identities, and religions in the last two weeks?",
                                                                                                          "If there are any, what was the nature of the statements?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_vote_buying_incidents", question_titles=["Have you heard or seen incidents of voters being encouraged not to vote or sell their voters cards?", 
                                                                                                   "If YES, when and where did this incidents of encouragement on not to vote happen?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_source_of_vote_buying", question_titles=["Who encouraged this?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_influence_on_voting_choices", question_titles=["Based on the campaign activities over the past two weeks, what do you think will influence people's voting choices in your area?"]),
                    
                    ## RISK OF VIOLENCE & CONFLICT
                    QuestionConfiguration(engagement_db_dataset="aik_incidents_of_polarisation", question_titles=["In the last two weeks, have some areas become no go areas for political supporters or ethnic groups.", 
                                                                                                                 "If YES, when and where did this happen, and who is being driven out?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_inability_to_work", question_titles=["Are there community members who have not been able to work in the last two weeks?", 
                                                                                                         "If YES, why has this happened to those community members?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_incidents_of_violence_and_polarisation", question_titles=["Have violent public protests or communal riots taken place?", 
                                                                                                                              "If YES, when, where and why did this public riots or communal riots happen?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_police_brutality", question_titles=["Have police officers used excessive force and / or live ammunition to respond to protesters?", 
                                                                                                        "If YES, when and where did this incident on police brutality happen?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_vandalism_theft_incidents", question_titles=["Have people's homes and assets been vandalized and/or stolen? "]),
                    QuestionConfiguration(engagement_db_dataset="aik_physical_harm", question_titles=["Have there been injuries and deaths related to elections activities in the last two weeks?", 
                                                                                                     "If YES, when and where did this election physical harm happen?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_sexual_assault", question_titles=["Have members of your community been sexually assaulted or raped related to elections activities in the last two weeks?", 
                                                                                                      "If YES, when and where did this sexual assault happen?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_violence_displacement", question_titles=["Has violence displaced members of your community?", 
                                                                                                             "If YES, when and where did this incidents of displacement happen?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_concern_about_safety_and_security", question_titles=["Based on the current political and security environment, are you concerned about safety and security within your community?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_peace_and_security_initiatives", question_titles=["Have you heard of Initiatives aimed at enhancing peace and security in the last two weeks?", 
                                                                                                                      "If YES, what were the peace and security initiatives?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_iebc_effectiveness", question_titles=["Independent Electoral and Boundaries Commission (IEBC)", "Add reason for the score on IEBC?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_nps_effectiveness", question_titles=["National Police Service", "Add reason for the score on NPS?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_ncic_effectiveness", question_titles=["National Cohesion and Integration Commission(NCIC)", "Add reason for the score on NCIC?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_dpp_effectiveness", question_titles=["Office of the Director of Public Prosecutions", "Add reason for the score on DPP?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_ipoa_effectiveness", question_titles=["Independent Policing Oversight Authority", "Add reason for the score on IPOA?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_judiciary_effectiveness", question_titles=["The Judiciary", "Add reason for the score on Judiciary?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_knchr_effectiveness", question_titles=["Kenya National Commission on Human Rights", "Add reason for the score on KNCHR?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_other_institutions_effectiveness", question_titles=["List other institutions and their ratings?"])
                ]
            )
        )
    ],
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
                    coda_dataset_id="AIK_voting_participation",
                    engagement_db_dataset="aik_voting_participation",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_voting_participation"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_voting_participation"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_willingness_to_help_victims",
                    engagement_db_dataset="aik_willingness_to_help_victims",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_willingness_to_help_victims"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_willingness_to_help_victims"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_engaging_authorities",
                    engagement_db_dataset="aik_engaging_authorities",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_engaging_authorities"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_engaging_authorities"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_incitement_sources",
                    engagement_db_dataset="aik_incitement_sources",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_incitement_sources"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_incitement_sources"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_vote_buying_incidents",
                    engagement_db_dataset="aik_vote_buying_incidents",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_vote_buying_incidents"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_vote_buying_incidents"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_source_of_vote_buying",
                    engagement_db_dataset="aik_source_of_vote_buying",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_source_of_vote_buying"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_source_of_vote_buying"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_incidents_of_polarisation",
                    engagement_db_dataset="aik_incidents_of_polarisation",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_incidents_of_polarisation"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_incidents_of_polarisation"
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
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_education",
                    engagement_db_dataset="aik_education",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_education"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_education"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_employment_status",
                    engagement_db_dataset="aik_employment_status",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_employment_status"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_employment_status"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_religion",
                    engagement_db_dataset="aik_religion",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_religion"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_religion"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_household_income",
                    engagement_db_dataset="aik_household_income",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_household_income"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_household_income"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_communities",
                    engagement_db_dataset="aik_communities",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_communities"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_communities"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="AIK_indigenous_or_minority",
                    engagement_db_dataset="aik_indigenous_or_minority",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/aik/aik_indigenous_or_minority"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="aik_indigenous_or_minority"
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
            make_rqa_analysis_dataset_config("aik_education", DatasetTypes.DEMOGRAPHIC),
            make_rqa_analysis_dataset_config("aik_employment_status", DatasetTypes.DEMOGRAPHIC),
            make_rqa_analysis_dataset_config("aik_religion", DatasetTypes.DEMOGRAPHIC),
            make_rqa_analysis_dataset_config("aik_communities", DatasetTypes.DEMOGRAPHIC),
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
            make_rqa_analysis_dataset_config("aik_voting_participation"),
            make_rqa_analysis_dataset_config("aik_willingness_to_help_victims"),
            make_rqa_analysis_dataset_config("aik_engaging_authorities"),
            make_rqa_analysis_dataset_config("aik_incitement_sources"),
            make_rqa_analysis_dataset_config("aik_vote_buying_incidents"),
            make_rqa_analysis_dataset_config("aik_source_of_vote_buying"),
            make_rqa_analysis_dataset_config("aik_incidents_of_polarisation"),
            make_rqa_analysis_dataset_config("aik_iebc_effectiveness"),
            make_rqa_analysis_dataset_config("aik_nps_effectiveness"),
            make_rqa_analysis_dataset_config("aik_ncic_effectiveness"),
            make_rqa_analysis_dataset_config("aik_dpp_effectiveness"),
            make_rqa_analysis_dataset_config("aik_ipoa_effectiveness"),
            make_rqa_analysis_dataset_config("aik_judiciary_effectiveness"),
            make_rqa_analysis_dataset_config("aik_knchr_effectiveness"),
            make_rqa_analysis_dataset_config("aik_other_institutions_effectiveness"),
            make_rqa_analysis_dataset_config("aik_electoral_violence_anxiety"),
            make_rqa_analysis_dataset_config("aik_hate_speech_and_actions_target"),
            make_rqa_analysis_dataset_config("aik_identity_groups_increase"),
            make_rqa_analysis_dataset_config("aik_inability_to_work"),
            make_rqa_analysis_dataset_config("aik_intolerance_incidents"),
            make_rqa_analysis_dataset_config("aik_peace_and_security_initiatives"),
            make_rqa_analysis_dataset_config("aik_physical_harm"),
            make_rqa_analysis_dataset_config("aik_police_brutality"),
            make_rqa_analysis_dataset_config("aik_political_environment"),
            make_rqa_analysis_dataset_config("aik_political_events_disruption"),
            make_rqa_analysis_dataset_config("aik_sexual_assault"),
            make_rqa_analysis_dataset_config("aik_unsafe_areas"),
            make_rqa_analysis_dataset_config("aik_vandalism_theft_incidents"),
            make_rqa_analysis_dataset_config("aik_violence_displacement"),
            make_rqa_analysis_dataset_config("aik_education"),
            make_rqa_analysis_dataset_config("aik_employment_status"),
            make_rqa_analysis_dataset_config("aik_religion"),
            make_rqa_analysis_dataset_config("aik_communities"),
            make_rqa_analysis_dataset_config("aik_indigenous_or_minority"),
        ],
        ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2022/AIK-ELECTIONS/"
    )
)
