def predict_future(money, income):

    future = money + income * 12 * 10

    return future



result = predict_future(
    50000,
    5000
)


print(result)