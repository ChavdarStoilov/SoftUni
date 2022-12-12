capacity_pool = int(input())
pipe1 = int(input())
pipe2 = int(input())
hour_missing_worker = float(input())

pipe1_filled = pipe1 * hour_missing_worker
pipe2_filled = pipe2 * hour_missing_worker

pool_filled = pipe2_filled + pipe1_filled
pool_filled_per_percentage = (pool_filled / capacity_pool) * 100

pipe1_filled_per_percentage = (pipe1_filled / pool_filled) * 100
pipe2_filled_per_percentage = (pipe2_filled / pool_filled) * 100

if pool_filled_per_percentage > 100:
    more_liters = pool_filled - capacity_pool
    print(f"For {hour_missing_worker:.2f} hours the pool overflows with {more_liters:.2f} liters.")
else:
    print(f"The pool is {pool_filled_per_percentage:.2f}% full. Pipe 1: {pipe1_filled_per_percentage:.2f}%. Pipe 2: {pipe2_filled_per_percentage:.2f}%.")