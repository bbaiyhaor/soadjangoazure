#encoding=utf-8
import sys
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
# with open('AMiner-Author.txt', 'r') as file:
# 	cnt = 0
# 	authors = []
# 	author = {}
# 	for line in file:
# 		cnt = (cnt + 1) % 10
# 		if (cnt == 1):
# 			author['index'] = line.strip().strip('#index ')
# 		elif (cnt == 2):
# 			author['name'] = line.strip().strip('#n ')
# 		elif (cnt == 6):
# 			author['hi'] = line.strip().strip('#hi ')
# 		elif (cnt == 9):
# 			author['domain'] = line.strip().strip('#t ').split(';')
# 		elif (cnt == 0):
# 			authors.append(author)
# 			print author
# 			author = {}
		


# with open('AMiner-Author.txt', 'r') as file:
# 	cnt = 0
# 	authors = {}
# 	author = {}
# 	for line in file:
# 		cnt = (cnt + 1) % 10
# 		if (cnt == 1):
# 			author['index'] = line.strip().strip('#index ')
# 		elif (cnt == 2):
# 			author['name'] = line.strip().strip('#n ')
# 		elif (cnt == 6):
# 			author['hi'] = line.strip().strip('#hi ')
# 		elif (cnt == 9):
# 			domains = line.strip().strip('#t ').split(';')
# 			for it in domains:
# 				if authors.has_key(it) == False:
# 					authors[it] = []
# 				authors[it].append(author)
# 		elif (cnt == 0):
# 			author = {}
# 			print authors



with open('AMiner-Author.txt', 'r') as file:
	cnt = 0
	tot = 0
	pro = ''
	for line in file:
		cnt = (cnt + 1) % 10
		if (cnt == 1):
			tot = tot + 1
			pro = 'pro' + str(tot)
			r.hset(pro, 'index', line.strip().strip('#index '))
		elif (cnt == 2):
			r.hset(pro, 'name', line.strip().strip('#n '))
		elif (cnt == 6):
			r.hset(pro, 'hi', line.strip().strip('#hi '))
		elif (cnt == 9):
			domains = line.strip().strip('#t ').split(';')
			for it in domains:
				r.sadd(it, pro)
		elif (cnt == 0):
			pass