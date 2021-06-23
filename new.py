# This programme is used to get the top 3 largest values from the dictionary values.
from heapq import nlargest
from operator import itemgetter


def function(dict):
	for item, value in nlargest(3, dict.items(), key= itemgetter(1)):
		print(item, value)


s = {"ankit":90, "Mom":89.3, "anjita":89.2, "ankita":23.34}
function(s)

