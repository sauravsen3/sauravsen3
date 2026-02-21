import numpy as np
from scipy.stats import norm
from black_scholes import compute_d1_d2


def delta(S, K, T, r, sigma, option_type="call"):
    """
    Delta — how much does the option price move per £1 move in the stock?

    Call delta: between 0 and 1
    Put delta:  between -1 and 0
    """
    d1, d2 = compute_d1_d2(S, K, T, r, sigma)

    if option_type == "call":
        return norm.cdf(d1)
    elif option_type == "put":
        return norm.cdf(d1) - 1


def gamma(S, K, T, r, sigma):
    """
    Gamma — rate of change of Delta per £1 move in stock.
    Same for both calls and puts.
    """
    d1, d2 = compute_d1_d2(S, K, T, r, sigma)

    return norm.pdf(d1) / (S * sigma * np.sqrt(T))


def vega(S, K, T, r, sigma):
    """
    Vega — how much does the option price change per 1% move in volatility?
    Same for both calls and puts.
    """
    d1, d2 = compute_d1_d2(S, K, T, r, sigma)

    return S * norm.pdf(d1) * np.sqrt(T) / 100


def theta(S, K, T, r, sigma, option_type="call"):
    """
    Theta — how much does the option lose in value per day?
    Almost always negative — time decay works against the option holder.
    """
    d1, d2 = compute_d1_d2(S, K, T, r, sigma)

    first_term = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))

    if option_type == "call":
        second_term = r * K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        second_term = r * K * np.exp(-r * T) * norm.cdf(-d2)

    return round((first_term - second_term) / 365, 4)


def rho(S, K, T, r, sigma, option_type="call"):
    """
    Rho — how much does the option price change per 1% move in interest rates?
    Calls have positive Rho, puts have negative Rho.
    """
    d1, d2 = compute_d1_d2(S, K, T, r, sigma)

    if option_type == "call":
        return (K * T * np.exp(-r * T) * norm.cdf(d2)) / 100
    elif option_type == "put":
        return (-K * T * np.exp(-r * T) * norm.cdf(-d2)) / 100


def all_greeks(S, K, T, r, sigma, option_type="call"):
    """
    Return all Greeks as a dictionary for a given option.
    """
    return {
        "Delta": delta(S, K, T, r, sigma, option_type),
        "Gamma": gamma(S, K, T, r, sigma),
        "Vega" : vega(S, K, T, r, sigma),
        "Theta": theta(S, K, T, r, sigma, option_type),
        "Rho"  : rho(S, K, T, r, sigma, option_type),
    }


# Test
if __name__ == "__main__":
    print(all_greeks(S=100, K=100, T=1, r=0.05, sigma=0.20, option_type="call"))
