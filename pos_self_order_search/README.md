# POS Self Order Search

This module adds search functionality to the POS Self Order interface in Odoo 18.0, restoring the search feature that was present in Odoo 17.0.

## Features

- Adds a search bar to the product list page in both mobile and desktop views
- Allows searching products by name and description
- Real-time filtering of products as you type
- Clean and modern UI that matches Odoo's design

## Installation

1. Copy this module to your Odoo addons directory
2. Update your addons list: Settings -> Update Apps List
3. Install the module: Apps -> search for "POS Self Order Search" -> Install

## Usage

The search functionality will be automatically available in the self-order interface after installation. Users can:

1. Click the search icon to show the search bar
2. Type to filter products in real-time
3. Click the X button or the search icon again to clear and hide the search bar

## Technical Details

This module extends the `pos_self_order` module by:

- Patching the ProductListPage component to add search functionality
- Adding a search input component to the product list interface
- Filtering products based on user input in real-time

## Dependencies

- pos_self_order

## License

LGPL-3 