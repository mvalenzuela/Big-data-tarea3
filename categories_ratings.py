from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import json
import time

start_time = time.time()

class JSONProtocol(object):

    def read(self, line):
        k_str, v_str = line.split('\t', 1)
        return json.loads(k_str), json.loads(v_str)

    def write(self, key, value):
        return '%s,%s' % (key, value)

class UsersCount(MRJob):

    #OUTPUT_PROTOCOL = JSONProtocol

    def mapper_userid(self, _, line):
        json_data = json.loads(line)
        if len(json_data) == 15:
            yield json_data["business_id"], ["categories_tag", json_data["name"], json_data["categories"]]
        else:
            yield json_data["business_id"], [json_data["stars"]]
    
    def reducer_1(self, business_id, data):
        data_list = [d for d in data]
        categories_list = []
        stars = []
        if len(data_list) > 1:
            for data in data_list:
                if data[0] == "categories_tag":
                    categories_list = data[2]
                else:
                    stars.append(data)
            for category in categories_list:    
                for star in stars:
                    yield category, star[0]

    def steps(self):
        return [MRStep(mapper=self.mapper_userid, reducer=self.reducer_1)]


if __name__ == '__main__':
    UsersCount.run()

print("--- %s seconds ---" % (time.time() - start_time)) 
