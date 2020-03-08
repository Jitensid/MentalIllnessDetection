
def get_all_responses(req):

	print(req)

	data = []

	length = len(req.get("queryResult").get("outputContexts"))

	for i in range(length):

		temp = req.get("queryResult").get("outputContexts")[i]

		if "parameters" in temp:

			data.append(temp["parameters"])

	return data