from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class Image(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image_file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['uploaded_at']),
            models.Index(fields=['user']),
        ]

    def __str__(self):
        username = self.user.username if self.user else 'Unknown user'
        return f"Image {self.id} uploaded by {username}"

class Style(models.Model):
    TYPE_CHOICES = [
        ('Expository_Cause_Effect', 'Expository - Cause and Effect'),
        ('Expository_Comparison', 'Expository - Comparison Essay'),
        ('Expository_Classification', 'Expository - Classification'),
        ('Expository_Descriptive', 'Expository - Descriptive'),
        ('Expository_Problem_Solution', 'Expository - Problem and Solution'),
        ('Expository_Process', 'Expository - Process'),
        ('Expository_Essay', 'Expository - Essay'),
        ('Expository_Anecdotal', 'Expository - Anecdotal'),
        ('Narrative', 'Narrative'),
        ('Narrative_Short_Story', 'Narrative - Short Story'),
        ('Narrative_Historical_Fiction', 'Narrative - Historical Fiction'),
        ('Narrative_Fable', 'Narrative - Fable'),
        ('Narrative_First_Person', 'Narrative - First Person Narrative'),
        ('Narrative_Epic_Poetry', 'Narrative - Epic Poetry'),
        ('Narrative_Memoir', 'Narrative - Memoir'),
        ('Narrative_Autobiography', 'Narrative - Autobiography'),
        ('Narrative_Fantasy', 'Narrative - Fantasy'),
        ('Narrative_Parable', 'Narrative - Parable'),
        ('Narrative_Narrative_History', 'Narrative - Narrative History'),
        ('Narrative_Epic', 'Narrative - Epic'),
        ('Persuasive', 'Persuasive'),
        ('Persuasive_Logos', 'Persuasive - Appeal to Reason/Logos'),
        ('Persuasive_Pathos', 'Persuasive - Appeal to Emotion/Pathos'),
        ('Persuasive_Ethos', 'Persuasive - Appeal to Character/Ethos'),
        ('Persuasive_Love_Letter', 'Persuasive - Love Letters'),
        ('Persuasive_Speech', 'Persuasive - Speeches'),
        ('Persuasive_Columns', 'Persuasive - Newspaper Columns'),
        ('Poetry', 'Poetry'),
        ('Poetry_Haiku', 'Poetry - Haiku'),
        ('Poetry_Free_Verse', 'Poetry - Free Verse'),
        ('Poetry_Sonnet', 'Poetry - Sonnet'),
        ('Poetry_Acrostic', 'Poetry - Acrostic'),
        ('Poetry_Villanelle', 'Poetry - Villanelle'),
        ('Poetry_Limerick', 'Poetry - Limerick'),
        ('Poetry_Ode', 'Poetry - Ode'),
        ('Poetry_Ballad', 'Poetry - Ballad'),
        ('Creative', 'Creative'),
        ('Creative_Script', 'Creative - Movie/TV Script'),
        ('Creative_Song', 'Creative - Song'),
        ('Creative_Short_Story', 'Creative - Short Story'),
        ('Creative_Memoir', 'Creative - Memoir'),
        ('Review', 'Review'),
        ('Review_Book', 'Review - Book Review'),
        ('Review_Movie', 'Review - Movie Review'),
        ('Review_TV_Show', 'Review - TV Show Review'),
        ('Review_Product', 'Review - Product Review'),
        ('Review_Travel', 'Review - Travel Review'),
        ('Technical', 'Technical'),
        ('Technical_Brochure', 'Technical - Brochure'),
        ('Technical_User_Guide', 'Technical - User Guide'),
        ('Technical_Proposal', 'Technical - Proposal'),
        ('Technical_Tech_Report', 'Technical - Tech Report'),
        ('Technical_SOP', 'Technical - Standard Operating Procedure'),
    ]

    TONE_CHOICES = [
        ('Absurd', 'Absurd'),
        ('Acerbic', 'Acerbic'),
        ('Admiring', 'Admiring'),
        ('Aggrieved', 'Aggrieved'),
        ('Ambivalent', 'Ambivalent'),
        ('Amused', 'Amused'),
        ('Animated', 'Animated'),
        ('Apathetic', 'Apathetic'),
        ('Apologetic', 'Apologetic'),
        ('Appreciative', 'Appreciative'),
        ('Ardent', 'Ardent'),
        ('Arrogant', 'Arrogant'),
        ('Assertive', 'Assertive'),
        ('Awestruck', 'Awestruck'),
        ('Benevolent', 'Benevolent'),
        ('Candid', 'Candid'),
        ('Caustic', 'Caustic'),
        ('Cautionary', 'Cautionary'),
        ('Celebratory', 'Celebratory'),
        ('Chatty', 'Chatty'),
        ('Colloquial', 'Colloquial'),
        ('Comic', 'Comic'),
        ('Compassionate', 'Compassionate'),
        ('Complex', 'Complex'),
        ('Compliant', 'Compliant'),
        ('Concerned', 'Concerned'),
        ('Conciliatory', 'Conciliatory'),
        ('Confused', 'Confused'),
        ('Critical', 'Critical'),
        ('Curious', 'Curious'),
        ('Cynical', 'Cynical'),
        ('Defensive', 'Defensive'),
        ('Defiant', 'Defiant'),
        ('Derisive', 'Derisive'),
        ('Detached', 'Detached'),
        ('Dignified', 'Dignified'),
        ('Diplomatic', 'Diplomatic'),
        ('Disapproving', 'Disapproving'),
        ('Direct', 'Direct'),
        ('Dispassionate', 'Dispassionate'),
        ('Distressing', 'Distressing'),
        ('Docile', 'Docile'),
        ('Earnest', 'Earnest'),
        ('Egotistical', 'Egotistical'),
        ('Empathetic', 'Empathetic'),
        ('Encouraging', 'Encouraging'),
        ('Enthusiastic', 'Enthusiastic'),
        ('Evasive', 'Evasive'),
        ('Excited', 'Excited'),
        ('Facetious', 'Facetious'),
        ('Farcical', 'Farcical'),
        ('Flippant', 'Flippant'),
        ('Forceful', 'Forceful'),
        ('Formal', 'Formal'),
        ('Frank', 'Frank'),
        ('Gentle', 'Gentle'),
        ('Grim', 'Grim'),
        ('Gullible', 'Gullible'),
        ('Hard', 'Hard'),
        ('Humble', 'Humble'),
        ('Humorous', 'Humorous'),
        ('Hypercritical', 'Hypercritical'),
        ('Impartial', 'Impartial'),
        ('Impassioned', 'Impassioned'),
        ('Imploring', 'Imploring'),
        ('Impressionable', 'Impressionable'),
        ('Inane', 'Inane'),
        ('Incredulous', 'Incredulous'),
        ('Indignant', 'Indignant'),
        ('Informative', 'Informative'),
        ('Inspirational', 'Inspirational'),
        ('Intense', 'Intense'),
        ('Intimate', 'Intimate'),
        ('Ironic', 'Ironic'),
        ('Irreverent', 'Irreverent'),
        ('Jaded', 'Jaded'),
        ('Joyful', 'Joyful'),
        ('Laudatory', 'Laudatory'),
        ('Light-Hearted', 'Light-Hearted'),
        ('Loving', 'Loving'),
        ('Macabre', 'Macabre'),
        ('Mourning', 'Mourning'),
        ('Nostalgic', 'Nostalgic'),
        ('Objective', 'Objective'),
        ('Obsequious', 'Obsequious'),
        ('Optimistic', 'Optimistic'),
        ('Outspoken', 'Outspoken'),
        ('Pensive', 'Pensive'),
        ('Persuasive', 'Persuasive'),
        ('Pessimistic', 'Pessimistic'),
        ('Philosophical', 'Philosophical'),
        ('Playful', 'Playful'),
        ('Pragmatic', 'Pragmatic'),
        ('Pretentious', 'Pretentious'),
        ('Regretful', 'Regretful'),
        ('Resigned', 'Resigned'),
        ('Restrained', 'Restrained'),
        ('Reverent', 'Reverent'),
        ('Righteous', 'Righteous'),
        ('Satirical', 'Satirical'),
        ('Sarcastic', 'Sarcastic'),
        ('Sensationalistic', 'Sensationalistic'),
        ('Sentimental', 'Sentimental'),
        ('Sincere', 'Sincere'),
        ('Skeptical', 'Skeptical'),
        ('Solemn', 'Solemn'),
        ('Sympathetic', 'Sympathetic'),
        ('Thoughtful', 'Thoughtful'),
        ('Tolerant', 'Tolerant'),
        ('Tragic', 'Tragic'),
        ('Unassuming', 'Unassuming'),
        ('Uneasy', 'Uneasy'),
        ('Urgent', 'Urgent'),
        ('Virtuous', 'Virtuous'),
        ('Whimsical', 'Whimsical'),
        ('Witty', 'Witty'),
        ('Wonder', 'Wonder'),
        ('World-Weary', 'World-Weary'),
        ('Worried', 'Worried'),
        # ... Add more tones as needed
    ]

    VOICE_CHOICES = [
        ('Shakespeare', 'William Shakespeare'),
        ('Emerson', 'Ralph Waldo Emerson'),
        ('Sherer', 'Michael W. Sherer'),
        ('Shelley', 'Mary Shelley'),
        ('Austen', 'Jane Austen'),
        ('Hemingway', 'Ernest Hemingway'),
        ('Orwell', 'George Orwell'),
        ('Rowling', 'J.K. Rowling'),
        ('Tolkien', 'J.R.R. Tolkien'),
        ('Dickens', 'Charles Dickens'),
        ('Fitzgerald', 'F. Scott Fitzgerald'),
        ('Poe', 'Edgar Allan Poe'),
        ('Angelou', 'Maya Angelou'),
        ('Frost', 'Robert Frost'),
        ('Woolf', 'Virginia Woolf'),
        ('Joyce', 'James Joyce'),
        ('Plath', 'Sylvia Plath'),
        ('Yeats', 'William Butler Yeats'),
        ('Eliot', 'T.S. Eliot'),
        ('Hughes', 'Langston Hughes'),
        ('Steinbeck', 'John Steinbeck'),
        ('Whitman', 'Walt Whitman'),
        ('Pound', 'Ezra Pound'),
        ('Homer', 'Homer'),
        ('Virgil', 'Virgil'),
        ('Milton', 'John Milton'),
        ('Dante', 'Dante Alighieri'),
        ('Goethe', 'Johann Wolfgang von Goethe'),
        ('Pushkin', 'Alexander Pushkin'),
        ('Neruda', 'Pablo Neruda'),
        # ... Add more voices as needed
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=True)
    tone = models.CharField(max_length=50, choices=TONE_CHOICES, blank=True)
    voice = models.CharField(max_length=100, choices=VOICE_CHOICES, blank=True)
    length = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return f"Style: {self.type} - {self.tone} by {self.voice}"

class ImageAnalysis(models.Model):
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    analyzed_at = models.DateTimeField(default=timezone.now)
    characteristics = models.JSONField(default=dict)

    def __str__(self):
        return f"Analysis for Image {self.image.id}"

class GeneratedText(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='generated_texts')
    style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name='generated_texts')
    text = models.TextField()

    def __str__(self):
        return f"Generated Text for Image {self.image.id} with Style {self.style.id}"

    def clean(self):
        """ Custom validation to ensure the text adheres to specified style length """
        if len(self.text.split()) > self.style.length:
            raise ValidationError(f"The text exceeds the maximum allowed length of {self.style.length} words.")
