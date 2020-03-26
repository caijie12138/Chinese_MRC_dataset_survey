import json
import argparse

def take_a_look(data_file):
    with open(data_file,'r') as reader:
        data = json.load(reader)
        article_count = 0
        question_count = 0
        article_len = 0
        for article in data['data']:
            article_count += 1
            for paragraph in article['paragraphs']:
                article_len += len(paragraph['context'])
                for query in paragraph['qas']:
                    question_count += 1
        return article_len/article_count,question_count,article_count

def take_a_look_for_baike(data_file):
    with open(data_file,'r') as reader:
        

def take_a_look_for_cmrc_2019(data_file):
    with open(data_file,'r') as reader:
        data = json.load(reader)
        article_count = 0
        choice_count = 0
        article_len = 0
        choice_len = 0
        for article in data['data']:
            article_count += 1
            article_len += len(article['context'])
            choice_count += len(article['choices'])
            for choice in article['choices']:
                choice_len += len(choice)
        choice_avg_len = choice_len / choice_count

        return article_len/article_count,choice_count/article_count,choice_avg_len

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file',required=True,help='the file path that you want take a look')
    args = parser.parse_args()
    if 'cmrc2019' in args.data_file:
        avg_article_len,question_count,choice_avg_len = take_a_look_for_cmrc_2019(args.data_file)
        print('article average len: %f' % avg_article_len)
        print('question average count: %d' % question_count)
        print('choice average len: %d' % choice_avg_len)
    elif 'baike' in args.data_file:
        avg_article_len, question_count, choice_avg_len = take_a_look_for_baike(args.data_file)
        print('article average len: %f' % avg_article_len)
        print('question average count: %d' % question_count)
        print('choice average len: %d' % choice_avg_len)
    else:
        avg_article_len, question_count, article_count = take_a_look(args.data_file)
        print('article average len: %f' % avg_article_len)
        print('article_count: %d' % article_count)
        print('question_count: %d' % question_count)



