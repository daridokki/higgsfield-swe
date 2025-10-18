class CreditManager:
    def __init__(self, total_budget=100.00):
        self.total_budget = total_budget
        self.used_budget = 0.0
        # Actual Higgsfield pricing from documentation
        # $1 = 16 credits, so 1 credit = $0.0625
        self.estimated_costs = {
            'nano-banana': 0.09,      # Text-to-image (1.5 credits = $0.09)
            'kling-2-5': 0.25,         # Image-to-video Kling 2.5 Turbo (4 credits = $0.25)
            'minimax-t2v': 0.50        # Text-to-video Minimax T2V (8 credits = $0.50)
        }
    
    def can_afford(self, model_type, operation_count=1):
        """Check if we have enough budget for the operation"""
        cost_per_operation = self.estimated_costs.get(model_type, 0.10)
        total_cost = cost_per_operation * operation_count
        return (self.used_budget + total_cost) <= self.total_budget
    
    def add_usage(self, model_type, operations=1):
        """Record usage and deduct from budget"""
        cost_per_operation = self.estimated_costs.get(model_type, 0.10)
        cost = cost_per_operation * operations
        self.used_budget += cost
        print(f"Used ${cost:.2f} for {model_type}. Total used: ${self.used_budget:.2f}")
        return self.used_budget
    
    def get_remaining_budget(self):
        """Get remaining budget"""
        return self.total_budget - self.used_budget
    
    def get_usage_percentage(self):
        """Get percentage of budget used"""
        return (self.used_budget / self.total_budget) * 100