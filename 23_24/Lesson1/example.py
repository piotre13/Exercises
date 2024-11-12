import pprint as pp
import json

def mean(ls, k , o, disc=0.5, *params, **kparams):
	avg = sum(ls)/len(ls)
	return avg

def read_json(path):
	with open(path, 'r') as fp:
		data = json.load(fp)
	return data

if __name__ == '__main__':

	list1 = [3,5,6,7,8]
	list2 = [3,6,54,6,78,9]
	k = 4
	o = 're'
	pp.pprint(list1)
	avg1 = mean(list1,o,k, disc=0.8, )
	avg2 = mean(list2)

	print(avg1)