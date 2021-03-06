import React from 'react';

import { mountWithContexts } from '@testUtils/enzymeHelpers';

import JobDetail from './JobDetail';

describe('<JobDetail />', () => {
  const mockDetails = {
    name: 'Foo',
  };

  test('initially renders succesfully', () => {
    mountWithContexts(<JobDetail job={mockDetails} />);
  });

  test('should display a Close button', () => {
    const wrapper = mountWithContexts(<JobDetail job={mockDetails} />);

    expect(wrapper.find('Button[aria-label="close"]').length).toBe(1);
    wrapper.unmount();
  });
});
