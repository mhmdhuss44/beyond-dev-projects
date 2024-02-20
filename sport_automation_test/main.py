from infra.youtube_infra import browserWrapper

if __name__ == '__main__':
    wrapper = browserWrapper()

    # Load configurations from the JSON file


    # Get all configurations and print them
    configurations = wrapper.get_all_configurations()
    print("All Configurations:")
    print(configurations)