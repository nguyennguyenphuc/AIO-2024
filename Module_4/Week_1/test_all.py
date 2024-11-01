# Import các hàm từ các file bài tập
from prepare_data import prepare_data, get_column
from linear_regression_one_sample import (
    initialize_params, predict, compute_loss, compute_gradient_wi,
    compute_gradient_b, update_weight_wi, update_weight_b
)
from linear_regression_n_samples import implement_linear_regression_nsamples
from linear_regression_restructured import prepare_data as prepare_data_restructured, predict as predict_restructured
from min_max_scaling import min_max_scaling

# Test các hàm trong prepare_data.py
def test_prepare_data():
    X, y = prepare_data('advertising.csv')
    assert len(X[0]) == 200, "TV data length should be 200"
    assert len(X[1]) == 200, "Radio data length should be 200"
    assert len(X[2]) == 200, "Newspaper data length should be 200"
    assert len(y) == 200, "Sales data length should be 200"
    print("test_prepare_data passed!")

# Test các hàm trong linear_regression_one_sample.py
def test_initialize_params():
    w1, w2, w3, b = initialize_params()
    assert w1 == 0.016992259082509283
    assert w2 == 0.0070783670518262355
    assert w3 == -0.002307860847821344
    assert b == 0
    print("test_initialize_params passed!")

def test_predict():
    y = predict(1, 1, 1, 0, 0.5, 0, 0.5)
    assert y == 1.0, "Prediction result should be 1.0"
    print("test_predict passed!")

def test_compute_loss():
    loss = compute_loss(1, 0.5)
    assert loss == 0.25, "Loss should be 0.25 for y_hat=1, y=0.5"
    print("test_compute_loss passed!")

def test_gradient_and_update():
    gradient_wi = compute_gradient_wi(1.0, 1.0, 0.5)
    gradient_b = compute_gradient_b(2.0, 0.5)
    updated_wi = update_weight_wi(1.0, gradient_wi, 1e-5)
    updated_b = update_weight_b(0.5, gradient_b, 1e-5)

    assert gradient_wi == -1.0
    assert gradient_b == -3.0
    assert round(updated_wi, 5) == 1.00001, "Updated wi should be 1.00001"
    assert round(updated_b, 5) == 0.50003, "Updated b should be 0.50003"
    print("test_gradient_and_update passed!")

# Test các hàm trong linear_regression_n_samples.py
def test_linear_regression_nsamples():
    X, y = prepare_data('advertising.csv')
    w1, w2, w3, b, losses = implement_linear_regression_nsamples(X, y, epoch_max=10, lr=1e-5)
    assert len(losses) == 10, "Loss list length should match epoch_max"
    print(f"Final weights: w1={w1}, w2={w2}, w3={w3}, b={b}")
    print("test_linear_regression_nsamples passed!")

# Test các hàm trong linear_regression_restructured.py
def test_prepare_data_restructured():
    X, y = prepare_data_restructured('advertising.csv')
    assert len(X[0]) == 4, "Each feature set should have four items (x0, x1, x2, x3)"
    assert len(X) == 200, "X should have 200 samples"
    print("test_prepare_data_restructured passed!")

def test_predict_restructured():
    X_features = [1, 230.1, 37.8, 69.2]
    weights = [0, 0.016992, 0.007078, -0.002308]
    y_hat = predict_restructured(X_features, weights)
    assert round(y_hat, 4) == 3.9275, f"Prediction should be approximately 3.9275, got {y_hat}"
    print("test_predict_restructured passed!")

# Test các hàm trong min_max_scaling.py
def test_min_max_scaling():
    data1 = [10, 20, 30]
    data2 = [5, 15, 25]
    data3 = [1, 2, 3]
    scaled_data, (max1, max2, max3, min1, min2, min3) = min_max_scaling(data1, data2, data3)

    assert scaled_data[0] == [0.0, 0.5, 1.0], f"Scaled data1 incorrect: {scaled_data[0]}"
    assert scaled_data[1] == [0.0, 0.5, 1.0], f"Scaled data2 incorrect: {scaled_data[1]}"
    assert scaled_data[2] == [0.0, 0.5, 1.0], f"Scaled data3 incorrect: {scaled_data[2]}"
    print("test_min_max_scaling passed!")

# Chạy tất cả các bài kiểm tra
if __name__ == "__main__":
    test_prepare_data()
    test_initialize_params()
    test_predict()
    test_compute_loss()
    test_gradient_and_update()
    test_linear_regression_nsamples()
    test_prepare_data_restructured()
    test_predict_restructured()
    test_min_max_scaling()
