from django.db import models
from django.contrib.auth.models import User

class UserPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios')
    opportunity = models.ForeignKey('Opportunity', on_delete=models.CASCADE, related_name='user_portfolios')
    invested_amount = models.DecimalField(max_digits=20, decimal_places=2)  # USD value
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    current_yield = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        db_table = 'user_portfolio'

    def __str__(self):
        return f"{self.user.username} - {self.opportunity.name}"
