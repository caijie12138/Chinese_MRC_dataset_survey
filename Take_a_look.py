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



if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file',required=True,help='the file path that you want take a look')
    args = parser.parse_args()
    avg_article_len,question_count,article_count = take_a_look(args.data_file)
    print('article average len: %f' % avg_article_len)
    print('article_count: %d' % article_count)
    print('question_count: %d' % question_count)



