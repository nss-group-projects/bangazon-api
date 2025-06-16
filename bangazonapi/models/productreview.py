from django.db import models


class ProductReview(models.Model):

    customer = models.ForeignKey(
        "Customer", on_delete=models.DO_NOTHING, related_name="reviews"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="reviews"
    )
    review = models.TextField()
    created_date = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"{self.product.name}: {self.review}"
