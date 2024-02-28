from app.tf_inference import generate
from app.yaml_parser import validate_and_fix_yaml
from app.adopt_generation import adopt_generation

if __name__ == '__main__':
    # input_sentence = "Find all italian restaurants that are no more than 200 meters from a fountain in London."
    # input_sentence = "Find supermarkets whose height is larger than 10"
    # input_sentence = "find me restaurants in berlin"
    # input_sentence = "find me wind turbine in bonn"
    # input_sentence="show me all shops with a name that contains the letters *\u00e5rden on Str\u00f8get in Kopenhagen"
    input_sentence = "find all malls with name zara in bonn"
    input_sentence = "find all bouldering gyms close to a river in berlin"
    input_sentence = "Find me a KFC 10m away from a pizza hut 10m away from a restaurant called al sultan in Augsburg."
    input_sentence = "Find me all bus stops 100m away from a highway bridge in Bonn"
    input_sentence = "Find a park in Perugia with a viewpoint and a drinking fountain."
    raw_output = generate(input_sentence)

    print("===raw_output===")
    print(raw_output)

    parsed_result = validate_and_fix_yaml(raw_output)

    print("====parsed result====")
    print(parsed_result)

    result = adopt_generation(parsed_result)

    print("===adopted result====")
    print(result)

