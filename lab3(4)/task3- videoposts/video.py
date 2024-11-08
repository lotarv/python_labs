def split_videos(n,k, durations):
    total_time = sum(durations)
    if total_time % k != 0:
        return "Нет"

    #Каждый пост одинаковой продолжительности

    target = total_time // k
    current_sum = 0
    post_sizes = []
    current_count = 0 #Количество видео в текущем посте

    for duration in durations:
        current_sum += duration
        current_count += 1

        if current_sum > target:
            return "Нет"
        elif current_sum == target:
            post_sizes.append(current_count)
            current_count = 0
            current_sum = 0
    
    if sum(post_sizes) == n and len(post_sizes) == k:
        return f"Да\n{" ".join(map(str, post_sizes))}"
    else:
        return "Нет"


#Примеры:
print("Пример1: n=6,k=3, durations = [3,3,1,4,1,6]")
print("Результат: ")
            