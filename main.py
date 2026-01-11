"""
Co-Simulation Framework for Cross-Domain Interactions
Testing energy systems, mobility networks, and telecommunications domains
"""

import helics as h
import logging
from scenarios.scenario_e1 import run_scenario_e1


def main():
    """
    Main entry point for the co-simulation framework.
    Runs six distinct scenarios to validate cross-domain interactions.
    """
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    
    logger.info("Co-Simulation Framework Initialized")
    logger.info("=" * 70)
    logger.info("Available Scenarios:")
    logger.info("E1. Smart Grid with Renewable Integration")
    logger.info("E2. [Not yet implemented]")
    logger.info("E3. [Not yet implemented]")
    logger.info("E4. [Not yet implemented]")
    logger.info("E5. [Not yet implemented]")
    logger.info("E6. [Not yet implemented]")
    logger.info("=" * 70)
    
    # Run Scenario E1
    logger.info("\nRunning Scenario E1...")
    report = run_scenario_e1()
    
    logger.info("\nAll scenarios completed!")


if __name__ == "__main__":
    main()
