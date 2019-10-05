def secret_share(tensor, workers, crypto_provider, precision_fractional=3):
    """
    Transform to fixed precision and secret share a tensor
    """
    return (
        tensor
            .fix_precision(precision_fractional=precision_fractional)
            .share(*workers, crypto_provider=crypto_provider,
                   requires_grad=True)
    )
