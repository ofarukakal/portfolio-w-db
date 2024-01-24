/*
CREATE TABLE `project` (
  `project_name` varchar(255) DEFAULT NULL,
  `project_description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`project_name`)
) 
*/

/*
INSERT INTO `project` VALUES ('Worldwide Terrorism Analysis', 'One of the biggest problems of countries is terrorism. In this analysis, I used a dataset that includes all terrorist incidents recorded from 1970 to 2017. I have analyzed all worldwide terrorist attacks.');
INSERT INTO 'project' VALUES ('Covid-19 Analysis', 'The COVID-19 epidemic, which emerged in Wuhan, China on November 17, 2019, has locked life all over the world for about 2 years. In my analysis, I analyzed the deaths and cases until 15 October 2022 on a country-by-country basis across the world.');
INSERT INTO 'project' VALUES ('Rental House Analysis',"In this project, I analyzed one of Turkey's biggest problems, rental house prices, and created a dataset with Web Scraping using Python and Selenium libraries on sahibinden.com. And I made an analysis using Python and visualized using Power BI.");
INSERT INTO 'project' VALUES ('CO2 Emission Analysis','One of the biggest causes of CO2 emissions is cars. In this project I did, I analyzed CO2 emissions car brands and models.');
*/

DELETE FROM project WHERE project_name = '?';

