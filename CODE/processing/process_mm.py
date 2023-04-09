from collections import defaultdict
from queue import Queue
from threading import Thread
from MetaMapWrapper import MetaMapWrapper
import json
from cleantext import clean
import math

def do_stuff(q, outfile):
    while q is not None:
        for i,data in enumerate(q):
            try:
                # data = q.get()
                preprocessed_post = {}
                text_to_annotate = ''
                preprocessed_post['post_group'] = data['post_group']
                preprocessed_post['post_url'] = data['post_url']
                preprocessed_post['post_title'] = data['post_title']
                text_to_annotate += data['post_title']
                preprocessed_post['post_time'] = data['post_time']
                preprocessed_post['post_follow_count'] = data['post_follow_count']
                preprocessed_post['post_author'] = data['post_author']
                preprocessed_post['post_author_profile'] = data['post_author_profile']
                preprocessed_post['post_like_count'] = data['post_like_count']
                preprocessed_post['post_reply_count'] = data['post_reply_count']
                preprocessed_post['post_content'] = data['post_content']
                text_to_annotate += ' ' + data['post_content']

                comments = ''
                if 'post_comments' in data:
                    post_comments = data['post_comments']
                    for comment in post_comments:
                        comment_content = comment['comment_content']
                        comment_content = comment_content.replace("\n", " ")
                        comments += ' ' + comment_content
                    text_to_annotate += ' ' + comments
                preprocessed_post['post_comments'] = comments
                if len(text_to_annotate) > 0:
                    # important: remove non-ASCII chars as MetaMap causes tagging issue
                    text_to_annotate = clean(text_to_annotate)
                    extracted_data = mmw.annotate(text_to_annotate)

                    if 'symptoms' in extracted_data:
                        preprocessed_post['symptoms'] = extracted_data['symptoms']
                    if 'diseases' in extracted_data:
                        preprocessed_post['diseases'] = extracted_data['diseases']
                    if 'diagnostics' in extracted_data:
                        preprocessed_post['diagnostic_procedures'] = extracted_data['diagnostics']
                with open(outfile, 'a+') as f:
                    json.dump(preprocessed_post, f, indent=4)
                    f.write(',\n')
                    q.task_done()
            except Exception as e:
                print("Exception while indexing this forum post: " + str(data))
                print('Exception message: ' + str(e))

        


num_threads = 4
q = []
mmw = MetaMapWrapper()

json_urls = defaultdict(bool)

with open('patient_info_forum_posts_content.json','r') as f:
    data = json.load(f)

        
split_length = math.floor(len(data)/num_threads)


q.append(data[0:37563])
q.append(data[37563:75126])
q.append(data[75126:112689])
q.append(data[112689:])

for i in range(num_threads):
    worker = Thread(target=do_stuff, args=(q[i],"outfile{}.json".format(i),))
    worker.daemon = False
    worker.start()






    # q[i].join()
    # print("Batch " + str(i) + " Done")
