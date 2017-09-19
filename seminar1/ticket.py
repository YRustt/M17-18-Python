def get_nearest_lucky_ticket(ticket_number):
    def is_lucky_ticket(ticket_number):
        digits = [(ticket_number // 10 ** i) % 10 for i in range(6)]
        return sum(digits[:3]) == sum(digits[3:])

    t_right, t_left = ticket_number, ticket_number

    while (t_right < 10 ** 6) and not is_lucky_ticket(t_right):
        t_right += 1

    while (t_left > 10 ** 5) and not is_lucky_ticket(t_left):
        t_left -= 1

    if (t_right >= 10 ** 6) or (t_right - ticket_number > ticket_number - t_left):
        return t_left
    else:
        return t_right
