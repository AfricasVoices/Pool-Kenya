from core_data_modules.cleaners import swahili

from src.pipeline_configuration_spec import *


PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="Create-Kenya-Pool",
    description="Creates the Kenya Pool from Porticus, AIK, GIZ, ICL",
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
                    FlowResultConfiguration("porticus_s01_demogs", "pool_kenya_location", "location"),
                    FlowResultConfiguration("porticus_s01_demogs", "pool_kenya_gender", "gender"),
                    FlowResultConfiguration("porticus_s01_demogs", "pool_kenya_age", "age"),
                    FlowResultConfiguration("porticus_s01_demogs", "pool_kenya_disabled", "disabled"),
                    FlowResultConfiguration("porticus_s01_demogs", "preferred_language", "preferred_language"),

                    FlowResultConfiguration("porticus_s01e01_activation", "rqa_s01e01", "porticus_s01e01"),
                    FlowResultConfiguration("porticus_s01e02_activation", "rqa_s01e02", "porticus_s01e02"),
                    FlowResultConfiguration("porticus_s01e03_activation", "rqa_s01e03", "porticus_s01e03"),
                    FlowResultConfiguration("porticus_s01e04_activation", "rqa_s01e04", "porticus_s01e04"),
                    FlowResultConfiguration("porticus_s01e05_activation", "rqa_s01e05", "porticus_s01e05"),
                    
                    FlowResultConfiguration("porticus_s01_evaluation_activation", "porticus_s01_evaluation", "porticus_s01_evaluation"),
                    FlowResultConfiguration("porticus_s01_closeout_activation", "porticus_s01_close_out", "porticus_s01_closeout"),
                ],
            )
        ),
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

                    FlowResultConfiguration("AIK_pool_invitation_activation", "aik_pool_invitation_2022", "aik_pool_invitation_2022"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_political_participation", "aik_political_participation"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_election_conversations", "aik_election_conversations"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_influence_on_voting_choices", "aik_influence_on_voting_choices"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_concern_about_safety_and_security", "aik_concern_about_safety_and_security"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_incidents_of_violence_and_polarisation", "aik_incidents_of_violence_and_polarisation"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_electoral_sexual_gender_based_violence", "aik_electoral_sexual_gender_based_violence"),
                    FlowResultConfiguration("AIK_survey_01_sms_ad", "aik_response_to_electoral_related_insecurity", "aik_response_to_electoral_related_insecurity"),

                    FlowResultConfiguration("AIK_survey_02_sms_ad", "aik_political_participation_2", "aik_political_participation_2"),
                    FlowResultConfiguration("AIK_survey_02_sms_ad", "aik_election_conversations_2", "aik_election_conversations_2"),
                    FlowResultConfiguration("AIK_survey_02_sms_ad", "aik_influence_on_voting_choices_2", "aik_influence_on_voting_choices_2"),
                    FlowResultConfiguration("AIK_survey_02_sms_ad", "aik_concern_about_safety_and_security_2", "aik_concern_about_safety_and_security_2"),
                    FlowResultConfiguration("AIK_survey_02_sms_ad", "aik_incidents_of_violence_and_polarisation_2", "aik_incidents_of_violence_and_polarisation_2"),
                    FlowResultConfiguration("AIK_survey_02_sms_ad", "aik_electoral_sexual_gender_based_violence_2", "aik_electoral_sexual_gender_based_violence_2"),
                    FlowResultConfiguration("AIK_survey_02_sms_ad", "aik_response_to_electoral_related_insecurity_2", "aik_response_to_electoral_related_insecurity_2"),
                ],
            )
        ),
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/pool-kenya-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("giz_s01_demogs", "pool_kenya_location", "location"),
                    FlowResultConfiguration("giz_s01_demogs", "pool_kenya_gender", "gender"),
                    FlowResultConfiguration("giz_s01_demogs", "pool_kenya_age", "age"),
                    FlowResultConfiguration("giz_s01_demogs", "pool_kenya_disabled", "disabled"),

                    FlowResultConfiguration("giz_s01e01_activation", "rqa_s01e01", "giz_s01e01"),
                    FlowResultConfiguration("giz_s01e02_activation", "rqa_s01e02", "giz_s01e02"),
                    FlowResultConfiguration("giz_s01e03_activation", "rqa_s01e03", "giz_s01e03"),
                    FlowResultConfiguration("giz_s01e04_activation", "rqa_s01e04", "giz_s01e04"),
                    FlowResultConfiguration("giz_s01e05_activation", "rqa_s01e05", "giz_s01e05"),
                    FlowResultConfiguration("giz_s01e06_activation", "rqa_s01e06", "giz_s01e06")
                ],
            )
        ),
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
                    FlowResultConfiguration("icl_machakos_poll_registration_activation_2022",
                                            "icl_machakos_poll_registration_2022",
                                            "machakos_poll_registration_2022"),
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
        ),
    ],
    google_form_sources=[
        GoogleFormSource(
            # https://docs.google.com/forms/d/e/1FAIpQLSekTlWRokfBg5WELobu6LsMIPR5BcBudKo6-TIs_2mi0sbnxQ/viewform
            google_form_client=GoogleFormsClientConfiguration(
                credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json"
            ),
            sync_config=GoogleFormToEngagementDBConfiguration(
                form_id="1xWV-X_pzn-niFODjcpb90Oq65EbhF9DXL5nfEn_Nz9U",
                question_configurations=[
                    QuestionConfiguration(engagement_db_dataset="age", question_titles=["How old are you?"]),
                    QuestionConfiguration(engagement_db_dataset="gender", question_titles=["What is your gender?"]),
                    QuestionConfiguration(engagement_db_dataset="location", question_titles=["Which ward do you currently live in?"]),
                    QuestionConfiguration(engagement_db_dataset="disabled", question_titles=["Do you have any form of disability?"]),

                    QuestionConfiguration(engagement_db_dataset="porticus_s01e01", question_titles=["What are the three priority developments that you would like the County Government to implement in your ward in the next five years?"]),
                    QuestionConfiguration(engagement_db_dataset="porticus_s01e02", question_titles=["What projects can Kitui, Machakos and Makueni counties collaborate in to advance the region?"]),
                    QuestionConfiguration(engagement_db_dataset="porticus_s01e03_intro", question_titles=["What ways do you use to participate in the decision making processes in your county?"]),
                    QuestionConfiguration(engagement_db_dataset="porticus_s01e03", question_titles=["What can your county government do to improve your participation in the county's decision making process?"]),
                ]
            )
        ),
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
                    QuestionConfiguration(engagement_db_dataset="age", question_titles=["How old are you?"]),
                    QuestionConfiguration(engagement_db_dataset="gender", question_titles=["What is your sex?"]),
                    QuestionConfiguration(engagement_db_dataset="location", question_titles=["Which constituency do you live in?"]),
                    QuestionConfiguration(engagement_db_dataset="disabled", question_titles=["Do you have any form of disability?"]),
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
                    QuestionConfiguration(engagement_db_dataset="age", question_titles=["Do you mind telling me how old you are?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_education", question_titles=["What is the highest level of education attained ? "]),
                    QuestionConfiguration(engagement_db_dataset="aik_employment_status", question_titles=["What is your employment Status ?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_religion", question_titles=["What is your religion ?"]),
                    QuestionConfiguration(engagement_db_dataset="gender", question_titles=["What is your sex? "]),
                    QuestionConfiguration(engagement_db_dataset="aik_household_income", question_titles=["Approximately what is your gross monthly household income? (I.e. This is the combined monthly income of all your household members). This will help us in determining your social-economic class."]),
                    QuestionConfiguration(engagement_db_dataset="disabled", question_titles=["Do you have any form of disability? (If disability is visible, do not ask, make the judgement)"]),
                    QuestionConfiguration(engagement_db_dataset="aik_communities", question_titles=["What community do you belong to?"]),
                    QuestionConfiguration(engagement_db_dataset="aik_indigenous_or_minority", question_titles=["Is it considered indigenous or minority?  if yes provide details."]),
                    QuestionConfiguration(engagement_db_dataset="location", question_titles=["Can I presume that you are currently a resident of; …………… County? [mention name of the target county]", 
                                                                                                       "Can I presume that you are currently a resident of; …………… Sub-County / Constituency? [mention name of the target sub-county]",
                                                                                                       "Can I presume that you are currently a resident of; …………… Ward? [mention name of the target ward]"]),
                    ## GENERAL ELECTORAL ENVIRONMENT
                    QuestionConfiguration(engagement_db_dataset="aik_voting_participation", question_titles=["Do you plan on voting in the August 9th General Elections?", "If NOT, why are you not planning to vote? "]),
                    QuestionConfiguration(engagement_db_dataset="aik_political_participation", question_titles=["Do you feel comfortable participating in any political activities in your area of residence?", 
                                                                                                               "Reasons for your answer on political activities participation."]),
                    QuestionConfiguration(engagement_db_dataset="aik_political_environment", question_titles=["Do you think the political and security environment is conducive to free and fair elections?"]),

                    ## HATE SPEECH AND INCITEMENT
                    QuestionConfiguration(engagement_db_dataset="aik_election_conversations", question_titles=["In your view, have elections-related conversations become more controversial and conflictual in the past two weeks than the two weeks before?"]),
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
    ]
)
