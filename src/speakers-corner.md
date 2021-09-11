# Speakers' Corner

Named after the renowned corner of Hyde Park in London, the Speakers' Corner seminars are a platform for everyone who would like to share their research.
Do you have a new preprint and want to create an accompanying video lecture or just a cool result you would like to share with the community? Speakers' corner allows you to create, advertise and share your talk via Virtual Science Forum platform.

### Give a talk
The series is hence on a "self-invitation" basis, where you register for giving a talk through the [Registration Form](https://github.com/virtualscienceforum/virtualscienceforum/issues/new?template=speakers_corner_application.md&labels=speakers_corner&title=Speakers%27%20corner%20talk%20application) and
bring your own audience. Every week, an announcement email is sent to the Speakers' Corner mailing list (register [here](mailinglist.md)) 
containing all of the upcoming talks. That way, more potential participants will learn about your talk and may decide to join.

??? info "How it works"

    1. Pick the topic of your talk, date and time (must be at least two weeks in the future), and make sure all your co-authors know about your presentation and agree.
    2. Fill in the [Registration Form](https://github.com/virtualscienceforum/virtualscienceforum/issues/new?template=speakers_corner_application.md&labels=speakers_corner&title=Speakers%27%20corner%20talk%20application)
    3. VSF:
        - checks availability of your time slot and confirm the date
        - creates the zoom meeting, opens the registration, and gives you the host key
    4. Advertising your talk:
        - make sure to **advertise your talk at your institution** and **invite participants to register for the talk**
        - tweet at @VirtualSciForum with the hashtag #VSFSpeakersCorner and we will retweet your talk info
        - VSF announces your talk in the VSF Speakers' Corner mailing list and on this website
    5. Preparing for your talk:
        - check that your screen resolution is set to lower than 1080p. This ensures the video captured by your camera while you speak will be not appear too small in the recording.
    6. You are welcome to moderate your talk yourself as well as invite a colleague to be your moderator
    7. VSF records your talk, forwards it to you for approval, and publishes it in the [YouTube channel](https://www.youtube.com/channel/UCvQEx4iW7u_x3jX742kUZLw)

{% set sc_talks = talks | sort(attribute="time") | selectattr("event_type", "==", "speakers_corner") | list %}
{% set upcoming = sc_talks | selectattr("time", ">", now()) | list %}
{% set previous = sc_talks | selectattr("time", "<", now()) | list %}

{% if upcoming %}
## Schedule

All times are shown in <span id="timezone">UTC</span> timezone.

|   Date   |     Speaker    | Title |
|:---------:|:--------------:|:-----:|
{%- for talk in upcoming | sort(attribute="time") %}
| <time datetime="{{ talk.time.isoformat() }}">{{ talk.time.strftime("%B %-d %-H:%M %Z") }}</time> | {{ talk.speaker_name }} | [{{ talk.title }}](#{{ talk.title | lower | a }}) |
{%- endfor %}

## Upcoming talks

{% for talk in upcoming | sort(attribute="time") %}
### {{ talk.title }}
#### {{ talk.speaker_name }} ({{ talk.speaker_affiliation }})

{% for line in talk.abstract.split("\n") -%}
> {{ line }}
{%- endfor %}
>
> **Authors:** {{ talk.authors }}  
{% if talk.preprint %}> **Preprint:** [arXiv:{{ talk.preprint }}](https://arxiv.org/abs/{{ talk.preprint }}){% endif %}

{% if talk.registration_url %}
If the form below doesn't work, [register directly]({{ talk.registration_url }})

<iframe width="100%" height="940" src="{{ talk.registration_url }}" frameborder="0" marginheight="0" marginwidth="0" style="overflow-x:hidden"></iframe>
{% endif %}
{% endfor %}
{% else %}
## Upcoming talks

There are no upcoming talks at the moment, apply [here](https://github.com/virtualscienceforum/virtualscienceforum/issues/new?template=speakers_corner_application.md&labels=speakers_corner&title=Speakers%27%20corner%20talk%20application) to present one.

{% endif %}

## Recordings

|     Speaker    | Title |
|:--------------:|:-----:|
{%- for talk in previous | sort(attribute="time", reverse=True) %}
| {{ talk.speaker_name }} | [{{ talk.title }}](#{{ talk.title | a }}) |
{%- endfor %}

{% for talk in previous | sort(attribute="time", reverse=True) %}

### {{ talk.title }}
**By {{ talk.speaker_name }} ({{ talk.speaker_affiliation }})**

===! "Details"

    **Authors:** {{ talk.authors }}  
    **Preprint:** [arXiv:{{ talk.preprint }}](https://arxiv.org/abs/{{ talk.preprint }})

    {{ talk.abstract | indent(width=4) }}

{% if talk.youtube_id %}

=== "Video recording"

    <iframe width="100%" height="315" src="https://www.youtube-nocookie.com/embed/{{ talk.youtube_id }}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% endif %}

{% endfor %}
