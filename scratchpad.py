weight = 0.7
def neural_network(input, weight):
    prediction = input * weight
    return prediction
age_of_person = [3, 13, 23, 33, 43, 53, 63, 73, 83, 93]
input = age_of_person[0]
pred = neural_network(input,weight)
print(pred)