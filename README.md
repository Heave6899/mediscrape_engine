This is a search engine that has been optimized to search various blog posts like WebMD and Patient.Info, filter posts based on symptoms and diseases, and suggest related symtoms the user can possibly have.

Created by:
Vansh Patel,
Bhargav Saravia,
Charles Kuo (Chia-Cheng Kuo),
Akash Arasu

Created for:
CSE 573 - Semantic Web Mining

Project Topic - Mining Healthcare Websites
Project Group - 3

Steps to run the engine
1. Create a virtual env using the following command: `python3 -m venv venv` and activate it using `source venv/bin/activate`.
2. Install all requirements using following command: `pip install -r requirements.txt`.
3. Install scrapy and cd into CODE/crawlers/patient_info_crawler and follow instructions given there.
4. cd into mayo_clinic_crawler and follow instructions for crawler made in beautifulsoup and selenium.
5. cd into processing directory, and follow instructions given in the directory.
6. cd into server directory, and follow instructions given in the directory. Till this step, all necessary backend files are generated.
7. Install Metamap from National Library of Medicine, and change the path of dir in line 4 MetaMapWrapper.py within server directory. There are two modes, online and offline mode. Online annotate requires api key from NLM UMLS website. Offline requires instance of metamap running locally.
8. Install SKR_WEB_PYTHON_API from Metamap's site, compile the code in python using their instructions and add the sub module to the project.
9. Install Apache Solr, we tested it using v9.2.0.
10. Run Apache Solr using the following command in its bin directory: `solr -c`, this runs solr in cloud mode. Make a schema.xml using the files given in solr_config directory with the help of schema generator function of apache solr. Publish the changes and name the solr core as medical_docs.
11. cd into processing or wherever the merged_data.json file has been generated, and execute the following command: `curl 'http://localhost:8983/solr/medical_docs/update?commit=true' --data-binary @merged_data.json -H 'Content-type:application/json'`. This will take a few minutes and upload all the documents to solr core.
12. cd into the server directory and run server_flask.py in nohup mode if required for background processing. `nohup python server_flask.py &`. If all steps executed and you reached this step, the complete backend works
13. Install apache2 if not present, and host the webapp/build files locally to run the frontend. You can manually compile and run the frontend too. Install node modules if needed.

Screenshot of Frontend with Sample Query:
![Frontend with a sample query output](/CODE/webapp/images/Demo.gif)