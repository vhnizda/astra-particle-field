from pathlib import Path


def test_particle_flow_moves_inward_and_wraps_at_path_end():
    source = (Path(__file__).parents[1] / 'index.html').read_text()
    assert 'const FLOW_SPEED = .045' in source
    assert 's.t = (s.t - FLOW_SPEED * dt + 1) % 1' in source
    assert 'const p = pointOn(s.path, s.t)' in source


if __name__ == '__main__':
    test_particle_flow_moves_inward_and_wraps_at_path_end()
    print('PASS: particle flow is inward and wraps')
