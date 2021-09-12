from omegaconf import DictConfig


def build_templates(infra: DictConfig, provider_name: str):

    provider_config = infra.providers[provider_name]
    infra_config = infra.config
    iain = infra_config

    for config_key in infra.config:
        test = infra.config[config_key]
        iain = test
