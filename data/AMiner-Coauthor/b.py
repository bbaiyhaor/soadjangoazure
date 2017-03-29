#encoding=utf-8
import sys
import redis
r = redis.Redis(host='localhost', port=6379, db=0)

with open('AMiner-Coauthor.txt', 'r') as file:
	for line in file:
		co = line.strip().strip('#').split('\t')	
		r.hset(str(co[0]), str(co[1]), str(co[2]))
		r.hset(str(co[1]), str(co[0]), str(co[2]))
