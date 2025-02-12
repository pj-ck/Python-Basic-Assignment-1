'''
Q7. EC2 Recommendation
Python script that provides EC2 instance recommendations based on a given instance's type, size, and CPU utilization. The script will help in recommending appropriate EC2 instances for optimizing performance and costs based on the utilization metrics.
Input:
Current EC2 Instance: A string representing the instance type and size (e.g., t2.nano, t3.medium).
CPU Utilization: A percentage value representing the current CPU utilization (e.g., 40%).

The output will be a recommendation for a new EC2 instance based on the following logic:

Underutilized: If the CPU utilization is less than 20%, recommend a smaller instance.
Optimized: If the CPU utilization is between 20% and 80%, recommend the same instance size but suggest the latest generation instance type.
Overutilized: If the CPU utilization is greater than 80%, recommend a larger instance.
'''



INSTANCE_SIZES = ['nano', 'micro', 'small', 'medium', 'large', 
                  'xlarge', '2xlarge', '4xlarge', '8xlarge', 
                  '16xlarge', '32xlarge']

def recommend_instance(instance, cpu):
    family, size = instance.split('.')
    idx = INSTANCE_SIZES.index(size)

    if cpu < 20:
        status = 'Underutilized'
        recommendation = f"{family}.{INSTANCE_SIZES[idx - 1]}" if idx > 0 else "No smaller size"
    elif cpu <= 80:
        status = 'Optimized'
        recommendation = f"{family.replace('t2', 't3')}.{size}" if 't2' in family else instance
    else:
        status = 'Overutilized'
        recommendation = f"{family}.{INSTANCE_SIZES[idx + 1]}" if idx < len(INSTANCE_SIZES) - 1 else "No larger size"

    return status, recommendation

def print_table(data):
    widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    line = '+' + '+'.join('-' * (w + 2) for w in widths) + '+'

    print(line)
    for i, row in enumerate(data):
        print('| ' + ' | '.join(f'{item:<{widths[j]}}' for j, item in enumerate(row)) + ' |')
        if i == 0:
            print(line)
    print(line)


instance = input("Enter current EC2 instance (e.g., t2.large): ")
cpu = float(input("Enter current CPU utilization (%): "))

status, recommendation = recommend_instance(instance, cpu)

table = [
    ["Serial No.", "Current EC2", "CPU (%)", "Status", "Recommended EC2"],
    ["1", instance, f"{cpu}%", status, recommendation]
]

print_table(table)
