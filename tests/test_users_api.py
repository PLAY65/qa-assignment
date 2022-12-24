import allure
import random


def test_get_random_user(users_api):
    response = users_api.get("users")

    with allure.step("Request was send, let's watch response code"):
        assert response.status_code == 200, f"Wrong response code {response.status_code}"

    response = response.json()
    rand_idx = random.randrange(len(response))
    random_num = response[rand_idx]

    user_id = random_num['id']
    user_email = random_num['email']

    #Get a random user (userID), print out its email address as console to Allure Report
    with allure.step(f"Random user (userID) is {user_id} with email {user_email}"):
        assert user_id <= 10

    response_users_posts = users_api.get(f"posts?userId={user_id}")
    response_users_posts = response_users_posts.json()

    # Verify they contains a valid Post IDs (an Integer between 1 and 100)
    for i in response_users_posts:
        assert 1 <= i['id'] <= 100, "Wrong postId id beside of range"

    body = {
        "title": "Send a POST",
        "body": "Body for sending post",
        "userId": user_id
    }

    # post using same userID with a non-empty title and body
    response_post = users_api.post("posts", body)
    with allure.step(f"Let's check post response {response_post}"):
        assert response_post.status_code == 201, f"Wrong response code {response_post.status_code}"
        pass
