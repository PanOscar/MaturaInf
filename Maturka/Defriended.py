import facebook
a = "EAAErqnUJhQABABdehPZBKpPatJ8l1QxDS5tYwFfqvZASyrpvJkrZB5stMeYgWks0ygC" \
    "1fngNQSZABZBGZBKYHupsZA1s24OrR9ZAFXUKZAEqUhqvAec61FZCwN9gNimUNi7FxYuZ" \
    "CkDSm3ZAkW0KVK8LnSHLbjgGXxuSghdNBZBUrhstXyZBokiZCSOEWTu"
access_token = "329486084703488|2KZmd_owgN9zAyRFWwy8Ms9Y5Dk"
graph = facebook.GraphAPI(access_token)
friends = graph.get_object("me/friends")