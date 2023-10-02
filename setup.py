import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-celery-progress",
    version="1.0.5",
    author="Pradish Bijukchhe",
    author_email="pradishbijukchhe@gmail.com",
    description="A django app to monitor celery tasks with progress",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sandbox-pokhara/django-celery-progress",
    project_urls={
        "Bug Tracker": (
            "https://github.com/sandbox-pokhara/django-celery-progress/issues"
        ),
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    package_dir={"django_celery_progress": "django_celery_progress"},
    python_requires=">=3",
    install_requires=["Django", "celery", "redis"],
)
