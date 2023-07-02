# Stanford-Open-Police-Project-FL-
An exploratory analysis of the Stanford Open Police Project for Florida data file.  
 
Florida traffic stops from 2010 - 2016

Acknowledgements:
This dataset was kindly made available by the Stanford Open Policing Project. If you use it for a research publication, please cite their working paper:
E. Pierson, C. Simoiu, J. Overgoor, S. Corbett-Davies, V. Ramachandran, C. Phillips, S. Goel. (2017) “A large-scale analysis of racial disparities in police stops across the United States”.


Content:
On a typical day in the United States, police officers make more than 50,000 traffic stops. The Stanford Open Policing Project team is gathering, analyzing, and releasing records from millions of traffic stops by law enforcement agencies across the country. Their goal is to help researchers, journalists, and policymakers investigate and improve interactions between police and the public.
If you'd like to see data regarding other states, please go to https://www.kaggle.com/stanford-open-policing.


Column name	                Column meaning	                                                                                              Example value


id	                        The unique ID we assign to each stop. Contains the state and year.	                                          VT-2011-00012

state	                      The two-letter code for the state in which the stop occurred.	                                                VT

stop_date	                  The date of the stop, in YYYY-MM-DD format. Some states do not provide the exact stop date: 
                            for example, they only provide the year or quarter in which the stop occurred. For these states,              2011-11-27
                            stop_date is set to the date at the beginning of the period: for example, January 1 if only year 
                            is provided.	                                                                                                  

stop_time	                  The 24-hour time of the stop, in HH:MM format.	                                                              20:15

location_raw	              The original data value from which we compute the county (or comparably granular location) in                 Winooski
                            which the stop occurred. Not in a standardized format across states.	                                        
                  
county_name	                The standardized name of the county in which the stop occurred.	                                              Chittenden County

county_fips	                The standardized 5-digit FIPS code in which the stop occurred.	                                              50007

district	                  In several states (e.g., Illinois) the stop county cannot be inferred, but a comparably granular              ILLINOIS STATE POLICE 01
                            location can. This comparably granular location is stored in the district column. Most states do 
                            not have this column.	
                  
fine_grained_location	      Any higher-resolution data about where the stop occurred: e.g., milepost or address. Not                      90400 I 89 N; EXIT 15 MM90/40
                            standardized across states.	
                            
police_department	          The police department or agency that made the stop. Not in a standard format across states.	                  WILLISTON VSP

driver_gender	              The driver’s gender, as recorded by the trooper.                                                              M, F, or NA.	M

driver_age_raw	            The original data value from which we compute the driver’s age when they were stopped. May be age,            1988
                            birth year, or birth date. Not in a standard format across states.
                            
driver_age	                The driver’s age when they were stopped. Set to NA if less than 15 or greater than or equal to 100.	          23

driver_race_raw	            The original data value from which the driver’s standardized race is computed. Not in a standard              African American
                            format across states.
                            
driver_race	                The standardized driver race. Possible values are White, Black, Hispanic, Asian, Other, and NA, with          Black
                            NA denoting values which are unknown. Asian refers to Asian, Pacific Islander, and Indian. Native 
                            Americans/American Indians are included in the "other" category. Anyone with Hispanic ethnicity is 
                            classified as Hispanic, regardless of their recorded race.	
                            
violation_raw	              The violation committed by the driver, in the language of the original data. Not in a standard                Speeding (10–19 MPH Over Prima Facie Limit *)
                            format across states. Some stops have multiple violations.	
                            
violation	                  The violation committed by the driver, standardized into categories which are consistent across states.	      Speeding

search_conducted	          A TRUE/FALSE value indicating whether a search was performed.	                                                TRUE

search_type_raw	            The justification for the search, in the language of the original data. NA if no search was performed.       CONSENT SEARCH CONDUCTED
                            Not in a standard format across states. Some states have multiple justifications for a search.	
                            
search_type	                The normalized justification for the search. Where possible, this is standardized into categories           Consent
                            which are consistent across states. For example, if something is clearly a consent search, search_type 
                            is referred to as “Consent”.
                            
contraband_found	          A TRUE/FALSE value indicating whether a search was performed and contraband was found. FALSE if             TRUE
                            no search was performed.
                            
stop_outcome	             The outcome of the stop. Many states have idiosyncratic outcomes — for example, “CHP 215” in                 Citation
                           California — so this column is not standardized across states. “Citation” and “Warning” are the 
                           values which occur most commonly across states. If the stop has multiple outcomes, the most severe 
                           outcome is used. For example, if a stop resulted in a citation and a warning, stop_outcome would 
                           be “Citation”.
                           
is_arrested	               A TRUE/FALSE value indicating whether an arrest was made.	                                                  TRUE
