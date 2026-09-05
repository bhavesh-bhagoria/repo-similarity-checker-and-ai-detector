from django.db import models


class Repo(models.Model):
    url = models.URLField()
    status = models.CharField(max_length=20, default="pending")
    clone_path = models.CharField(max_length=500, null=True, blank=True)
    ai_score = models.FloatField(null=True, blank=True)
    checked_at = models.DateTimeField(null=True, blank=True)

class RepoFile(models.Model):
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE)
    path = models.CharField(max_length=500)
    language = models.CharField(max_length=50)
    fingerprint = models.JSONField(default=list)
    ai_score = models.FloatField(null=True, blank=True)

class SimilarityMatch(models.Model):
    repo_a = models.ForeignKey(Repo,
        on_delete=models.CASCADE,
        related_name="matches_as_a")
    repo_b = models.ForeignKey(Repo,
        on_delete=models.CASCADE,
        related_name="matches_as_b")
    score = models.FloatField()
    matched_files = models.JSONField(default=dict)