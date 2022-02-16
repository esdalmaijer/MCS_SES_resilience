
VAR_LABELS = { \
    # First layer (mostly sweep 1).
    "S1_SES_FA":                            "Socio-economic status", \
    "S1_SES_McClementsPovertyLine":         "Poverty", \
    "S1_Parent_Neighbourhood":              "Neighbourhood", \
    "S1_SES_EducationAvg":                  "Parent education", \
    "S1_SES_AverageLastJob":                "Parent occupation", \
    "S1_SES_Income_TotalHousehold":        "Parent income", \
    "AirPollution_Sulphur":                 "Pollution (sulphur)", \
    "AirPollution_Particularate":           "Pollution (particularate)", \
    "AirPollution_Nitrogen":                "Pollution (NOx)", \
    "AirPollution_CarbonMonoxide":          "Pollution (CO)", \
    "S1_Health_SmokedThroughoutPregnancy":  "Smoking (pregnancy)", \
    "S1_Health_CurrentSmoking":             "Smoking (current)", \
    "S1_Parent_AlcoholPregnant":            "Alcohol (pregnancy)", \
    "S1_Parent_AlcoholCurrent":             "Alcohol (current)", \
    "S1_Parent_GeneralHealth":              "Parent general health", \
    "S1_ParentMentalHealth":                "Parent mental health", \
    "S1_Parent_Health_AvgNorm":             "Parent health", \
    "S1_Parent_Mood_AvgNorm":               "Parent mood", \
    "S1_LocusControl":                      "Parent locus of control", \
    "S1_ParentSelfEsteem":                  "Parent self-esteem", \
    "S1_ParentLifeSatisfaction":            "Parent life satisfaction", \
    "S1_Parenting_Beliefs":                 "Parenting beliefs", \
    "S1_ParentRelationshipQuality":         "Parent relationship quality", \
    "S1_Fam_ParentsEverSeperated":          "Parents separated", \
    "S1_Fam_FatherPresent":                 "Father present", \
    "S1_Fam_PlannedPregnancy":              "Planned pregnancy", \
    "S1_Fam_NSiblings":                     "Number of siblings", \
    "S1_EarlyDevelopment":                  "Early development", \
    "S1_Health_BirthWeight":                "Birth weight", \
    "S1_Health_Height":                     "Birth height", \
    "S1_Health_DaysPreTerm":                "Days pre-term", \
    "S2_Sex":                               "Sex (is girl)", \

    # Second layer (sweep 2).
    "S2_NeighRating":                           "Neighbourhood", \
    "S2_Parenting":                             "Parenting (general)", \
    "S2_Parenting_Values_Rules":                "Parenting (rules)", \
    "S2_Parenting_Values_Enforcement":          "Parenting (enforcement)", \
    "S2_HarshParenting":                        "Harsh parenting", \
    "S2_ParentMentalHealth":                    "Parent mental health", \
    "S2_BrackenSchoolReadiness":                "School readiness", \
    "S2_Cog_VobabBASRawScore":                  "Vocabulary", \
    "S2_Behav_independence":                    "Independence)", \
    "S2_Behav_selfregulation":                  "Self-regulation)", \
    "S2_Behav_WorkThingsOutForSelf":            "Insight", \
    "S2_Behav_MoodSwings":                      "Mood swings", \
    "S2_Behav_DoesNotNeedMuchHelpWithTasks":    "Independence (tasks)", \
    "S2_Behav_GetsOverExcited":                 "Over excitedness", \
    "S2_Behav_ChoosesActivitiesOnTheirOwn":     "Independence (activities)", \
    "S2_Behav_EasilyFustrated":                 "Easily frustrated", \
    "S2_Behav_GetsOverBeingUpset":              "Gets over upset", \
    "S2_Behav_PersistsDifficultTasks":          "Persistance (tasks)", \
    "S2_Behav_MoveToNewActivity":               "New activity frequency", \
    "S2_Behav_ActsImpulsively":                 "Impulsivity", \
    "S2_SDQ_Emotion":                           "Emotional dysfunction", \
    "S2_SDQ_Conduct":                           "Conduct problems", \
    "S2_SDQ_Hyper":                             "Hyperactivity/inattention", \
    "S2_SDQ_Peer":                              "Peer relationship problems", \
    "S2_SDQ_Prosocial":                         "Prosocial behaviour", \

    # Third layer (sweep 3).
    "S3_HouseholdChaos":                        "Household chaos", \
    "S3_Parenting_HelpSchool":                  "Parenting (school help)", \
    "S3_Parenting_Activities":                  "Parenting (activities)", \
    "S3_Parenting_HelpSchool_FSN":              "Parenting (school help)", \
    "S3_Parenting_Activities_FSN":              "Parenting (activities)", \
    "S3_Parenting_Chaos_FSN":                   "Parenting (chaos)", \
    "S3_LifeSatisfaction":                      "Life satisfaction", \
    "S3_Cog_PatternAbilityScore":               "Cognition (patterns)", \
    "S3_Cog_PictureSimilaritiesAbility":        "Cognition (similarities)", \
    "S3_Cog_NamingVocabAbility":                "Cognition (vocabulary)", \
    "S3_Health_GeneralHealth":                  "Health (general)", \
    "S3_Health_FSN":                            "Health (physical)", \
    "S3_Parent_SDQ_Emotion":                    "Emotional dysfunction", \
    "S3_Parent_SDQ_Conduct":                    "Conduct problems", \
    "S3_Parent_SDQ_Hyper":                      "Hyperactivity/inattention", \
    "S3_Parent_SDQ_Peer":                       "Peer relationship problems", \
    "S3_Parent_SDQ_Prosocial":                  "Prosocial behaviour", \

    # Fourth layer (sweep 4).
    "S4_DigitalAccess":                         "Digital access", \
    "S4_TechAvailability":                      "Tech availability", \
    "S4_Par_Q_InternetAtHome":                  "Internet access", \
    "S4_Par_Q_HaveAccessToComputer":            "Computer access", \
    "S4_Par_Involvement":                       "Parenting (involvement)", \
    "S4_Par_Involvement_FSN":                   "Parenting (involvement)", \
    "S4_Par_Q_PhysicalPlay":                    "Physical play", \
    "S4_PhysicalPlay":                          "Physical play", \
    "S4_Cog_WordReadScore":                     "Cognition (reading)", \
    "S4_Cog_PatternRawScore":                   "Cognition (patterns)", \
    "S4_Cog_NumberSkillsRawScore":              "Cognition (numbers)", \
    "S4_Teach_creative":                        "Art/music (teacher-rating)", \
    "S4_Teach_English":                         "English (teacher-rating)", \
    "S4_Teach_STEM":                            "STEM (teacher-rating)", \
    "S4_Teach_PE":                              "PE (teacher-rating)", \
    "S4_Par_Q_ChildReadEnjoyment":              "Likes reading (home)", \
    "S4_SchoolLikeReading":                     "Likes reading (school)", \
    "S4_SchoolLikeSTEM":                        "Likes STEM (school)", \
    "S4_SchoolBullies":                         "Bullies others", \
    "S4_SchoolBullied":                         "Bullied by others", \
    "S4_SchoolLike":                            "School liking", \
    "S4_ChildQ_School_FA1_Interest_Norm":       "School (interest)", \
    "S4_ChildQ_School_FA2_Bullied_Norm":        "School (being bullied)", \
    "S4_ChildQ_School_FA3_WellBehaved_Norm":    "School (behaviour)", \
    "S4_ChildQ_Aspiration1":                    "Aspiration", \
    "S4_ChildQ_Friends_FSN":                    "Friends", \
    "S4_ChildQ_FeelAvg":                        "Feelings", \
    "S4_SDQ_Emotion":                           "Emotional dysfunction", \
    "S4_SDQ_Conduct":                           "Conduct problems", \
    "S4_SDQ_Hyper":                             "Hyperactivity/inattention", \
    "S4_SDQ_Peer":                              "Peer relationship problems", \
    "S4_SDQ_Prosocial":                         "Prosocial behaviour", \

    # Fifth layer (sweep 5).
    "S5_ChildQ_SportsGames":                    "Plays sports", \
    "S5_Teach_AA_PE":                           "PE (teacher-rating)", \
    "S5_Teach_school":                          "School aptitude (teacher-rating)", \
    "S5_Teach_creative":                        "Art/music (teacher-rating)", \
    "S5_Teach_English":                         "English (teacher-rating)", \
    "S5_Teach_STEM":                            "STEM (teacher-rating)", \
    "S5_Teach_Bullied":                         "Bullied by others (teacher-rating)", \
    "S5_Teach_BullyOthers":                      "Bullies others (teacher-rating)", \
    "S5_Cog_VS_Raw":                            "Cognition (vocabulary)", \
    "S5_Cog_SWM_TotalErrors48":                 "Cognition (working memory)", \
    "S5_ChildQ_Feelings_Happy":                 "Feelings (happiness)", \
    "S5_ChildQ_Feelings_Laugh":                 "Feelings (laughter)", \
    "S5_ChildQ_Feelings_Angry":                 "Feelings (anger)", \
    "S5_ChildQ_Feelings_Worry":                 "Feelings (worrying)", \
    "S5_ChildQ_Feelings_Sad":                   "Feelings (sadness)", \
    "S5_ChildQ_Feelings_Afraid":                "Feelings (fear)", \
    "S5_Parent_SDQ_Emotion":                    "Emotional dysfunction", \
    "S5_Parent_SDQ_Conduct":                    "Conduct problems", \
    "S5_Parent_SDQ_Hyper":                      "Hyperactivity/inattention", \
    "S5_Parent_SDQ_Peer":                       "Peer relationship problems", \
    "S5_Parent_SDQ_Prosocial":                  "Prosocial behaviour", \

    # Outcome layer (sweep 6).
    "S6_Cog_WordScore":                         "Cognition (vocabulary)", \
    "S6_RiskyBehaviours_Cig":                   "Smoking", \
    "S6_RiskyBehaviours_Alcohol":               "Alcohol", \
    "S6_IllegalBehav":                          "Illegal behaviour", \
    "S6_Drugs":                                 "Drug taking", \
    "S6_BullyPeople":                           "Bullies others", \
    "S6_ChildQ_Truancy_Ever":                   "Truancy", \
    "S6_ChildQ_SelfHarm":                       "Self-harm", \
    "S6_Wellbeing":                             "Wellbeing", \
    "S6_SelfEsteem":                            "Self-esteem", \
    "S6_Feelings":                              "Negative feelings", \
    "S6_NegFeelings":                           "Negative feelings", \
    "S6_Parent_SDQ_Emotion":                    "Emotional dysfunction", \
    "S6_Parent_SDQ_Conduct":                    "Conduct problems", \
    "S6_Parent_SDQ_Hyper":                      "Hyperactivity/inattention", \
    "S6_Parent_SDQ_Peer":                       "Peer relationship problems", \
    "S6_Parent_SDQ_Prosocial":                  "Prosocial behaviour", \
     }