from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/api/blogposts")

        for i in range(0,100):
          self.client.post("/api/blogpostcommands", json={"title": "Test blog entry" + str(i),
              "rawContent": "Example text number " + str(i), 
              "publicSlug": "SlugX",
              "draft": True,
              "category": "ENGINEERING",
              "broadcast": True,
              "publishAt": "2025-07-29T22:00:00.000Z"})