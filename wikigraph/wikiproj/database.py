import redis
import logging
import sys

class Redis:

	'''
	Initialize and connect to the Redis instance
	@string address: address the Redis instance is located.
	@int port: port the instance is located within the address.
	'''
	def __init__(self, address='127.0.0.1', port=6379):
		self.r = redis.StrictRedis(host=address, port=port, db=0)
		logging.info('Redis instance opened at address %s' % address)
	
	'''
	Returns the value associated with the given key in the database
	'''
	def get(self, key):
		return self.r.get(key)			

	'''
	Associates key with value in the database
	'''
	def set(self,key,val):
		self.r.set(key,val)

	def add_slist(self, name, member, score=1):
		self.r.zadd(name, score, member)

	'''
	Adds or increments the count of the value of a member in a sorted list
	'''
	def incr_slist(self, name, member):
		self.r.zincrby(name,member)

	def add_set(self, name, member):
		self.r.sadd(name,member)
		
	def is_member_set(self,name,member):
		return self.r.sismember(name, member)
	
	'''
	Returns integer of value associated with specific member
	'''
	def get_slist_val(self, name, member):
		return self.r.zscore(name, member)
	
	'''
	Returns the number of elements in the sorted list
	'''
	def get_slist_len(self,name):
		return self.r.scard(name)
		
	'''
	Returns a list of the elements in the given list
	'''
	def get_slist_members(self, name):
		return self.r.smembers(name)
	
	'''
	Returns true if the key exists in the database.
	'''
	def exists(self, key):
		return self.r.exists(key)
	
	'''
	Returns total keys in the database
	'''
	def length(self):
		return self.r.dbsize() #total number of keys
	
	'''
	Returns a (python) list of all of the keys in the database
	'''	
	def keys(self, pattern=''):
		return self.r.keys(pattern)