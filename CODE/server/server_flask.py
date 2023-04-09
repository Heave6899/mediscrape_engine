import json
from flask import Flask, jsonify, redirect, url_for, render_template, request
import requests
import urllib.parse as uparser
from MetaMapWrapper import MetaMapWrapper
from cleantext import clean
from AutocompleteWrapper import AutocompleteWrapper
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Enable CORS on all routes
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})

mmw = MetaMapWrapper()
acw = AutocompleteWrapper()


def annotate_extract_relate(q):
    """
    Annotate and extract disease-related information from a given text.

    Args:
        q (str): Text to be annotated.

    Returns:
        dict: A dictionary containing disease-related information extracted from the text.
    """
    text_to_annotate = clean(q.replace('"', '').replace(',', " and "))
    extracted_data = mmw.online_annotate(text_to_annotate)

    response_json = {}
    if 'symptoms' in extracted_data:
        response_json['symptoms'] = extracted_data['symptoms']
    if 'diseases' in extracted_data:
        response_json['diseases'] = extracted_data['diseases']
    if 'diagnostics' in extracted_data:
        response_json['diagnostic_procedures'] = extracted_data['diagnostics']
    print('r', response_json)
    response_json = acw.get_suggestions(response_json)
    return response_json


@app.route('/search_query', methods=['POST'])
def search_query():
    """
    Search the Solr index for a given query and return the extracted disease-related information.

    Returns:
        dict: A dictionary containing the search results and disease-related information extracted from the query.
    """
    if request.method == 'POST':
        domain_url = "http://localhost:8983/solr/medical_docs2/query?q={}&q.op=AND&indent=true&start={}&rows={}&sort=post_like_count%20desc,%20post_follow_count%20desc,%20post_reply_count%20desc"
        query = request.json['query']
        print("query", query)
        page = int(request.json.get('page'))-1 if request.json['page'] else 0

        # page = 0
        page_count = 10
        start_row = str(page*page_count)
        print('page', start_row)
        body = requests.get(domain_url.format(
            uparser.quote(query), start_row, page_count)).content
        resp = annotate_extract_relate(query)
        docs = json.loads(body)['response']['docs']
        for i in docs:
            i['post_content'][0] = clean(i['post_content'][0])
            i['post_title'][0] = clean(i['post_title'][0])
        return {'data': docs, 'disea': resp['disea'], 'syos': resp['syos']}
    else:
        return {'data': 'invalid query, use POST'}


@app.route('/auto_complete', methods=['GET'])
def flask_api():
    """
    Extract disease-related information from a given text.

    Returns:
        dict: A dictionary containing the disease-related information extracted from the text.
    """
    response = annotate_extract_relate(request.args.get('q'))
    return response


if __name__ == "__main__":
    app.run(port=5050, debug=True)
