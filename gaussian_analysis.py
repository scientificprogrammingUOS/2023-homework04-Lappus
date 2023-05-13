import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
        if not all(isinstance(x, (int, float)) for x in [loc, scale, lower_bound, upper_bound]):
              return f'All Attributes have to be integer or float!'
        elif lower_bound > upper_bound:
              return f'the lower_bound is not allowed to be bigger than the upper_bound'
        else:
            gaussian = np.random.normal(loc, scale, size=100)
            gaussian = gaussian[(gaussian >= lower_bound) & (gaussian <= upper_bound)]
            values = (gaussian.mean(), gaussian.std())
            
            return values

if __name__ == "__main__":
    # use this for your own testing!

    pass
