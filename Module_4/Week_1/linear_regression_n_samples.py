from linear_regression_one_sample import *
def implement_linear_regression_nsamples(X_data, y_data, epoch_max=50, lr=1e-5):
    """Linear regression using batch of N samples with MSE loss."""
    losses = []
    w1, w2, w3, b = initialize_params()
    N = len(y_data)

    for epoch in range(epoch_max):
        loss_total, dw1_total, dw2_total, dw3_total, db_total = 0, 0, 0, 0, 0

        for i in range(N):
            x1, x2, x3 = X_data[0][i], X_data[1][i], X_data[2][i]
            y = y_data[i]
            y_hat = predict(x1, x2, x3, w1, w2, w3, b)
            loss = compute_loss(y_hat, y)
            loss_total += loss
            dw1_total += compute_gradient_wi(x1, y, y_hat)
            dw2_total += compute_gradient_wi(x2, y, y_hat)
            dw3_total += compute_gradient_wi(x3, y, y_hat)
            db_total += compute_gradient_b(y, y_hat)

        w1 = update_weight_wi(w1, dw1_total / N, lr)
        w2 = update_weight_wi(w2, dw2_total / N, lr)
        w3 = update_weight_wi(w3, dw3_total / N, lr)
        b = update_weight_b(b, db_total / N, lr)

        losses.append(loss_total / N)
    return w1, w2, w3, b, losses
