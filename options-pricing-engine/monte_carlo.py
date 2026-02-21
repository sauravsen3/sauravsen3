import numpy as np

def monte_carlo_price(S, K, T, r, sigma, option_type="call", num_simulations=100000):
    """
    Price a European option using Monte Carlo simulation.
    Parameters:
        S               : float — current stock price
        K               : float — strike price
        T               : float — time to expiry in years
        r               : float — annual risk-free rate
        sigma           : float — annual volatility
        option_type     : str   — "call" or "put"
        num_simulations : int   — number of random paths to simulate
    Returns:
        dict — price, standard error, confidence interval
    """
    Z = np.random.standard_normal(num_simulations)
    S_T = S * np.exp((r - (sigma**2)/2) * T + sigma * np.sqrt(T) * Z)

    if option_type == "call":
        payoffs = np.maximum(S_T - K, 0)
    elif option_type == "put":
        payoffs = np.maximum(K - S_T, 0)

    discounted_payoffs = np.exp(-r * T) * payoffs

    price = np.mean(discounted_payoffs)
    std_error = np.std(discounted_payoffs) / np.sqrt(num_simulations)

    return {
        "price"        : round(price, 4),
        "std_error"    : round(std_error, 4),
        "conf_interval": (round(price - 1.96 * std_error, 4),
                          round(price + 1.96 * std_error, 4))
    }

# Test
if __name__ == "__main__":
    print(monte_carlo_price(S=100, K=100, T=1, r=0.05, sigma=0.20, option_type="call"))
