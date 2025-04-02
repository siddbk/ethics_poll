# Additional Scenarios - Examples for Extension

Below are additional ethical scenarios you can add to `config.py` to extend the game with more diverse ethical dilemmas. Each includes multiple options and framework positions.

## Workplace Monitoring

```python
{
    'id': 'scenario6',
    'title': 'AI Workplace Monitoring',
    'description': 'A company is considering implementing AI-powered monitoring software that tracks employee productivity, analyzes keyboard usage patterns, and monitors attention through webcams. How should this system be implemented?',
    'options': [
        {'id': 'A', 'text': 'Full implementation with continuous monitoring to maximize productivity'},
        {'id': 'B', 'text': 'Limited implementation with transparency about what is monitored and when'},
        {'id': 'C', 'text': 'Opt-in system where employees choose whether to participate'},
        {'id': 'D', 'text': 'No implementation, as such monitoring fundamentally violates employee dignity'}
    ],
    'frameworks': {
        'Utilitarianism': {
            'choice': 'B',
            'explanation': 'Limited transparent monitoring balances productivity gains with employee wellbeing.'
        },
        'Deontology': {
            'choice': 'D',
            'explanation': 'Constant surveillance treats employees as means to productivity ends rather than autonomous beings.'
        },
        'Rights-based': {
            'choice': 'C',
            'explanation': 'Employees have a right to privacy and should be able to choose whether to participate.'
        },
        'Justice-oriented': {
            'choice': 'B',
            'explanation': 'Transparency ensures fairness as all employees understand the rules applied to them.'
        }
    }
},
```

## Content Moderation

```python
{
    'id': 'scenario7',
    'title': 'AI Content Moderation',
    'description': 'A social media platform uses AI to automatically moderate user content. How aggressive should the content filtering be?',
    'options': [
        {'id': 'A', 'text': 'Remove only clearly illegal content, prioritizing free expression'},
        {'id': 'B', 'text': 'Remove harmful but legal content like misinformation and hate speech'},
        {'id': 'C', 'text': 'Proactively filter all potentially offensive content before it\'s posted'},
        {'id': 'D', 'text': 'Use human moderators instead of AI for all content decisions'}
    ],
    'frameworks': {
        'Utilitarianism': {
            'choice': 'B',
            'explanation': 'This balances harm reduction with maintaining useful discourse.'
        },
        'Rights-based': {
            'choice': 'A',
            'explanation': 'Free expression is a fundamental right that should only be limited in cases of clear harm.'
        },
        'Virtue Ethics': {
            'choice': 'C',
            'explanation': 'A virtuous platform would proactively protect users from harmful content.'
        },
        'Care Ethics': {
            'choice': 'D',
            'explanation': 'Human moderators can better understand context and show appropriate care for all parties.'
        }
    }
},
```

## AI in Education

```python
{
    'id': 'scenario8',
    'title': 'AI in Education',
    'description': 'A school district is implementing AI to personalize learning for students. The AI will track student performance, adjust curriculum difficulty, and recommend learning paths. How should student data be handled?',
    'options': [
        {'id': 'A', 'text': 'Collect and analyze all possible data to maximize personalization'},
        {'id': 'B', 'text': 'Collect limited data with parental consent and clear transparency'},
        {'id': 'C', 'text': 'Use anonymized data only with strict access controls'},
        {'id': 'D', 'text': 'Allow parents/students to opt out of data collection entirely'}
    ],
    'frameworks': {
        'Utilitarianism': {
            'choice': 'C',
            'explanation': 'This approach provides educational benefits while minimizing privacy risks.'
        },
        'Rights-based': {
            'choice': 'D',
            'explanation': 'Students and parents have a right to control their personal data.'
        },
        'Justice-oriented': {
            'choice': 'B',
            'explanation': 'This ensures benefits of personalization without creating disparities between students.'
        },
        'Care Ethics': {
            'choice': 'B',
            'explanation': 'This shows appropriate care for student development while respecting family agency.'
        }
    }
},
```

## AI Emotion Recognition

```python
{
    'id': 'scenario9',
    'title': 'AI Emotion Recognition',
    'description': 'A company has developed AI that claims to recognize human emotions from facial expressions and voice patterns. Where would it be ethical to deploy this technology?',
    'options': [
        {'id': 'A', 'text': 'Widely across settings including retail, job interviews, and customer service'},
        {'id': 'B', 'text': 'Only in sensitive settings like therapy with informed consent'},
        {'id': 'C', 'text': 'Only for research purposes with clear disclosure to participants'},
        {'id': 'D', 'text': 'This technology should not be deployed as it is inherently flawed and invasive'}
    ],
    'frameworks': {
        'Utilitarianism': {
            'choice': 'C',
            'explanation': 'Research use balances potential future benefits while minimizing immediate harms.'
        },
        'Deontology': {
            'choice': 'D',
            'explanation': 'Reading emotions without consent violates autonomy and treats people as objects to be analyzed.'
        },
        'Virtue Ethics': {
            'choice': 'B',
            'explanation': 'Used ethically in therapy, this technology could help develop empathy and emotional intelligence.'
        },
        'Rights-based': {
            'choice': 'D',
            'explanation': 'People have a right to emotional privacy and not to have their inner states interpreted by machines.'
        }
    }
},
```

## Predictive Policing

```python
{
    'id': 'scenario10',
    'title': 'Predictive Policing AI',
    'description': 'A police department wants to implement AI that predicts where crimes are likely to occur and which individuals might commit crimes based on historical data. Should they proceed?',
    'options': [
        {'id': 'A', 'text': 'Yes, to efficiently allocate resources and prevent crime'},
        {'id': 'B', 'text': 'Yes, but only for location prediction, not individual prediction'},
        {'id': 'C', 'text': 'Yes, but with robust oversight, transparency, and regular bias audits'},
        {'id': 'D', 'text': 'No, the risks of bias and civil rights violations outweigh potential benefits'}
    ],
    'frameworks': {
        'Utilitarianism': {
            'choice': 'C',
            'explanation': 'With proper oversight, this could reduce crime while minimizing harms.'
        },
        'Deontology': {
            'choice': 'D',
            'explanation': 'Pre-crime prediction fundamentally violates the principle of presumed innocence.'
        },
        'Justice-oriented': {
            'choice': 'D',
            'explanation': 'Historical data contains systemic biases that will be amplified, creating unjust outcomes.'
        },
        'Rights-based': {
            'choice': 'B',
            'explanation': 'Location prediction doesn\'t target individuals but still allows for resource optimization.'
        }
    }
},
```

## Medical Diagnosis AI

```python
{
    'id': 'scenario11',
    'title': 'AI Medical Diagnosis Errors',
    'description': 'An AI diagnostic system for cancer detection has a 95% accuracy rate, outperforming the average doctor\'s 90%. However, when the AI makes a mistake, it\'s much harder to understand why. Should hospitals adopt this system?',
    'options': [
        {'id': 'A', 'text': 'Yes, immediately replace human diagnosis with the more accurate AI'},
        {'id': 'B', 'text': 'Yes, but only as a second opinion alongside human doctors'},
        {'id': 'C', 'text': 'Only after the AI can provide explanations for its diagnostic decisions'},
        {'id': 'D', 'text': 'No, statistical accuracy isn\'t worth the loss of human judgment and accountability'}
    ],
    'frameworks': {
        'Utilitarianism': {
            'choice': 'B',
            'explanation': 'This maximizes accuracy while maintaining human oversight and responsibility.'
        },
        'Virtue Ethics': {
            'choice': 'C',
            'explanation': 'A virtuous approach requires understanding why decisions are made, not just their outcomes.'
        },
        'Care Ethics': {
            'choice': 'B',
            'explanation': 'This approach maintains the human care relationship while improving outcomes.'
        },
        'Rights-based': {
            'choice': 'C',
            'explanation': 'Patients have a right to understand the reasoning behind their diagnosis.'
        }
    }
},
```

## AI Personal Assistants

```python
{
    'id': 'scenario12',
    'title': 'AI Personal Assistants and Children',
    'description': 'AI personal assistants like voice assistants are increasingly used by children. How should these systems interact with children?',
    'options': [
        {'id': 'A', 'text': 'No different than with adults - children should learn to interact with AI naturally'},
        {'id': 'B', 'text': 'With special "kid-friendly" modes requiring parental activation'},
        {'id': 'C', 'text': 'With clear indicators that they are speaking to an AI, not a person'},
        {'id': 'D', 'text': 'These systems should be designed to minimize engagement with children'}
    ],
    'frameworks': {
        'Utilitarianism': {
            'choice': 'B',
            'explanation': 'Kid-friendly modes balance educational benefits with appropriate protections.'
        },
        'Virtue Ethics': {
            'choice': 'C',
            'explanation': 'Honesty about the nature of AI helps children develop authentic relationships.'
        },
        'Care Ethics': {
            'choice': 'D',
            'explanation': 'This prioritizes human relationships and care during crucial developmental stages.'
        },
        'Deontology': {
            'choice': 'C',
            'explanation': 'We have a duty not to deceive children about whether they're interacting with humans or machines.'
        }
    }
},
```

## Adding These Scenarios

To add these scenarios to your game:

1. Open `config.py` in your code editor
2. Copy any of these scenario objects into the `SCENARIOS` list
3. Save the file and restart the application
4. The new scenarios will appear in the admin panel

## Creating Your Own Scenarios

To create your own effective ethical scenarios:

1. **Choose relevant topics** for your audience:
   - Industry-specific dilemmas
   - Current AI controversies
   - Future technologies that raise ethical questions

2. **Craft balanced options** that represent different viewpoints:
   - Aim for 4 distinct ethical positions
   - Avoid obviously "right" or "wrong" choices
   - Present each position with its strongest reasoning

3. **Include framework positions** that show how different ethical approaches would evaluate the scenario:
   - Try to represent at least 3-4 different frameworks
   - Explain the reasoning behind each framework's position
   - Show how frameworks can lead to different conclusions

4. **Format correctly** in the Python dictionary structure:
   ```python
   {
       'id': 'your-scenario-id',
       'title': 'Concise Title',
       'description': 'Detailed description of the ethical dilemma...',
       'options': [
           {'id': 'A', 'text': 'First option'},
           {'id': 'B', 'text': 'Second option'},
           {'id': 'C', 'text': 'Third option'},
           {'id': 'D', 'text': 'Fourth option'}
       ],
       'frameworks': {
           'Framework Name': {
               'choice': 'A',  # Which option this framework would choose
               'explanation': 'Why this framework favors this option...'
           },
           # Add more frameworks...
       }
   }
   ```

## Testing New Scenarios

Before using new scenarios in your event:

1. Test with a small group to ensure:
   - The dilemma is easily understood
   - Options are clearly distinct
   - No obvious bias toward one answer
   - Options spark meaningful discussion

2. Refine based on feedback:
   - Clarify confusing language
   - Balance options that are too obviously right/wrong
   - Add nuance to oversimplified positions