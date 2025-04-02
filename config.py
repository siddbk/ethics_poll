"""
AI Ethics Poll Game - Configuration Settings

This module contains all the configuration settings for the application:
- Application settings (port, debug mode)
- Scenario definitions with ethical dilemmas
- Framework positions on each scenario
"""

# Application configuration
APP_CONFIG = {
    #'PORT': 5000,
    'DEBUG': False,
    'TITLE': 'AI Ethics Poll Game',
    'SUBTITLE': 'Exploring Ethical Dilemmas in AI',
}

# Framework list
FRAMEWORKS = {
    'Consequentialism': {
        'description': 'Evaluates AI decisions based on their outcomes and impacts',
        'approach': 'Would consider the net beneficial or harmful consequences of the AI system',
        'key_principle': 'The ends justify the means; maximize positive outcomes'
    },
    'Deontological Ethics': {
        'description': 'Focuses on adherence to moral rules and duties in AI design',
        'approach': 'Would assess whether the AI respects universal ethical principles regardless of outcomes',
        'key_principle': 'Some actions are inherently right or wrong, independent of consequences'
    },
    'Virtue Ethics': {
        'description': 'Emphasizes developing AI that embodies positive character traits',
        'approach': 'Would ask if the AI system promotes virtuous behaviors and intentions',
        'key_principle': 'Develop AI that demonstrates wisdom, fairness, and moderation'
    },
    'Rights-based Ethics': {
        'description': 'Prioritizes protecting fundamental human rights in AI development',
        'approach': 'Would evaluate whether the AI system respects human autonomy and dignity',
        'key_principle': 'AI must never violate fundamental human rights and freedoms'
    },
    'Fairness and Justice': {
        'description': 'Focuses on equitable treatment and resource distribution in AI systems',
        'approach': 'Would analyze whether the AI treats all stakeholders fairly and without bias',
        'key_principle': 'AI should promote equality and avoid perpetuating discrimination'
    },
    'Care Ethics': {
        'description': 'Centers on relationships, context, and empathy in AI decision-making',
        'approach': 'Would consider how the AI maintains human relationships and shows care',
        'key_principle': 'AI should prioritize human connection and compassionate outcomes'
    },
    'Transparency': {
        'description': 'Emphasizes explainability and openness in AI systems',
        'approach': "Would assess whether the AI's decisions can be understood and audited",
        'key_principle': 'AI processes should be explainable and accessible to stakeholders'
    },
    'Beneficence': {
        'description': 'Focuses on developing AI that actively promotes human wellbeing',
        'approach': 'Would evaluate whether the AI creates positive value for humanity',
        'key_principle': 'AI should be designed to benefit humans and enhance human capabilities'
    },
    'Non-maleficence': {
        'description': 'Prioritizes preventing harm in AI development and deployment',
        'approach': 'Would analyze potential risks and harms the AI might cause',
        'key_principle': 'First, do no harm; minimize negative impacts of AI systems'
    },
    'Autonomy': {
        'description': 'Values human choice and control in AI interactions',
        'approach': 'Would consider whether the AI preserves human agency and decision-making',
        'key_principle': 'Humans should maintain meaningful control over AI systems'
    }
}

# Example usage in the Flask application:
'''
@app.route('/reveal_frameworks/<scenario_id>')
def reveal_frameworks(scenario_id):
    scenario = get_scenario(scenario_id)
    relevant_frameworks = scenario.get('relevant_frameworks', [])
    framework_positions = {}
    
    for framework_name in relevant_frameworks:
        if framework_name in FRAMEWORKS:
            framework = FRAMEWORKS[framework_name]
            framework_positions[framework_name] = {
                'description': framework['description'],
                'position': scenario['framework_positions'].get(framework_name, 'No position available'),
                'approach': framework['approach']
            }
    
    return render_template('framework_reveal.html', 
                          scenario=scenario, 
                          frameworks=framework_positions)
'''

# Predefined scenarios with ethical dilemmas
SCENARIOS = [
    {
        'id': 'scenario1',
        'title': 'AI-Powered Healthcare Decisions',
        'description': 'A hospital is considering implementing an AI system that can prioritize patients in the emergency room based on their likelihood of survival and quality of life after treatment. Should they implement this system?',
        'options': [
            {'id': 'A', 'text': 'Yes, as long as the AI is proven to be more accurate than human doctors'},
            {'id': 'B', 'text': 'Yes, but only as a supporting tool with final decisions made by human doctors'},
            {'id': 'C', 'text': 'No, life-or-death decisions should only be made by humans'},
            {'id': 'D', 'text': 'No, this approach fundamentally devalues certain lives over others'}
        ],
        'frameworks': {
            'Utilitarianism': {
                'choice': 'A',
                'explanation': 'If the AI maximizes overall successful treatments, it produces the greatest good for the greatest number.'
            },
            'Deontology': {
                'choice': 'C',
                'explanation': 'Using an algorithm to determine who receives critical care violates the principle that humans should be treated as ends, not means.'
            },
            'Rights-based': {
                'choice': 'D',
                'explanation': 'All patients have an equal right to care, and algorithmic prioritization may compromise this equality.'
            },
            'Justice-oriented': {
                'choice': 'B',
                'explanation': 'This balances efficiency with the need for human oversight to ensure fair distribution of care.'
            }
        }
    },
    {
        'id': 'scenario2',
        'title': 'AI Surveillance for Public Safety',
        'description': 'A city is considering implementing AI-powered facial recognition cameras throughout public spaces to identify potential criminals and prevent crime. Should they proceed?',
        'options': [
            {'id': 'A', 'text': 'Yes, public safety outweighs privacy concerns in public spaces'},
            {'id': 'B', 'text': 'Yes, but with strict oversight, transparency, and limitations on data use'},
            {'id': 'C', 'text': 'No, the potential for misuse and bias outweighs security benefits'},
            {'id': 'D', 'text': 'No, mass surveillance fundamentally violates civil liberties regardless of implementation'}
        ],
        'frameworks': {
            'Utilitarianism': {
                'choice': 'B',
                'explanation': 'This option balances the utility of increased security with minimizing harms from surveillance.'
            },
            'Deontology': {
                'choice': 'D',
                'explanation': 'Mass surveillance treats people as suspects by default, violating the duty to respect autonomy.'
            },
            'Rights-based': {
                'choice': 'C',
                'explanation': 'The potential bias in these systems threatens equal protection and due process rights.'
            },
            'Justice-oriented': {
                'choice': 'B',
                'explanation': 'With proper oversight, the system can provide security while distributing potential harms fairly.'
            }
        }
    },
    {
        'id': 'scenario3',
        'title': 'AI in Hiring Decisions',
        'description': 'A company wants to use AI to screen job applicants based on patterns found in their existing high-performing employees. The AI would analyze resumes, social media, and other public data to rank candidates. Should they use this system?',
        'options': [
            {'id': 'A', 'text': 'Yes, AI can reduce human bias and find patterns humans might miss'},
            {'id': 'B', 'text': 'Yes, but only for initial screening with diverse human teams making final decisions'},
            {'id': 'C', 'text': 'No, the AI will likely perpetuate existing workforce biases'},
            {'id': 'D', 'text': 'No, using personal data like social media for hiring decisions is inherently invasive'}
        ],
        'frameworks': {
            'Utilitarianism': {
                'choice': 'B',
                'explanation': 'This creates the most overall value by combining AI efficiency with human judgment.'
            },
            'Virtue Ethics': {
                'choice': 'C',
                'explanation': 'A virtuous organization would recognize that patterns from past hiring may contain biases.'
            },
            'Rights-based': {
                'choice': 'D',
                'explanation': 'Candidates have a right to privacy and to be evaluated on relevant professional criteria only.'
            },
            'Justice-oriented': {
                'choice': 'B',
                'explanation': 'This provides a balance of efficiency while ensuring fair opportunity through human oversight.'
            }
        }
    },
    {
        'id': 'scenario4',
        'title': 'Autonomous Vehicles Ethical Choices',
        'description': 'When programming autonomous vehicles to handle unavoidable accidents, how should the AI prioritize who to protect?',
        'options': [
            {'id': 'A', 'text': 'Always prioritize the safety of the vehicle occupants'},
            {'id': 'B', 'text': 'Minimize total casualties regardless of whether they are in or outside the vehicle'},
            {'id': 'C', 'text': 'Protect the most vulnerable individuals (children, elderly) regardless of numbers'},
            {'id': 'D', 'text': 'Autonomous vehicles should not make ethical choices - this should be left to humans'}
        ],
        'frameworks': {
            'Utilitarianism': {
                'choice': 'B',
                'explanation': 'This approach maximizes overall welfare by minimizing total harm across all people.'
            },
            'Deontology': {
                'choice': 'D',
                'explanation': 'Moral decisions about whose life to prioritize should not be pre-programmed but left to human moral agents.'
            },
            'Virtue Ethics': {
                'choice': 'C',
                'explanation': 'A virtuous society would show special care for its most vulnerable members.'
            },
            'Rights-based': {
                'choice': 'B',
                'explanation': 'All persons have an equal right to life, so minimizing total casualties respects this equality.'
            }
        }
    },
    {
        'id': 'scenario5',
        'title': 'AI-Generated Content and Intellectual Property',
        'description': 'An AI system is trained on works by human artists and can generate new art in their style. Who should own the copyright to AI-generated artwork?',
        'options': [
            {'id': 'A', 'text': 'The creators of the AI system'},
            {'id': 'B', 'text': 'The person who prompted or directed the AI to create the work'},
            {'id': 'C', 'text': 'The original artists whose styles were used to train the AI'},
            {'id': 'D', 'text': 'AI-generated work should be in the public domain'}
        ],
        'frameworks': {
            'Utilitarianism': {
                'choice': 'B',
                'explanation': 'This creates incentives for both AI developers and users to produce valuable creative works.'
            },
            'Deontology': {
                'choice': 'C',
                'explanation': 'We have a duty to respect the creative work of artists and not appropriate their styles without consent.'
            },
            'Justice-oriented': {
                'choice': 'D',
                'explanation': 'The most equitable approach is to make AI-generated content available to all, particularly since the AI learns from collective human creation.'
            },
            'Rights-based': {
                'choice': 'C',
                'explanation': 'Artists have a right to control derivative works that build upon their distinct creative expressions.'
            }
        }
    }
]