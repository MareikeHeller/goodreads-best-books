def popularity_measures_plot_prep(df_input, group_by_cols, avg_rating_col=['average_rating'],
                                  award_col=['is_award_winning']):
    '''
    INPUT:
    df_input - a dataframe holding all the variables of interest
    group_by_cols - a list of strings holding the name of the column(s) the data should be grouped by
    avg_rating_col - a list holding the column with average readers' rating
    award_col - a list holding the column informing if book is an award winning book (1) or not (0)

    OUTPUT:
    df_grouped - a dataframe holding grouped popularity measures by group_by_cols

    THE FUNCTION calculates the following popularity measures by group_by_cols:
    1. book_count
    2. avg_rating_mean
    3. avg_rating_std
    4. award_winning_count
    5. award_winning_share

    Indices are group_by_cols.
    '''
    import pandas as pd
    from functools import reduce

    df_computing_avg_rating = group_by_cols + avg_rating_col
    df_computing_award = group_by_cols + award_col

    df_book_count = df_input[df_computing_avg_rating].groupby(group_by_cols).count().rename(
        columns={str(avg_rating_col[0]): 'book_count'})
    df_avg_rating_mean = df_input[df_computing_avg_rating].groupby(group_by_cols).mean().rename(
        columns={str(avg_rating_col[0]): 'avg_rating_mean'})
    df_avg_rating_std = df_input[df_computing_avg_rating].groupby(group_by_cols).std().rename(
        columns={str(avg_rating_col[0]): 'avg_rating_std'})
    df_award_count = df_input[df_computing_award].groupby(group_by_cols).sum().rename(
        columns={str(award_col[0]): 'award_winning_count'})

    df_singles = [df_book_count, df_avg_rating_mean, df_avg_rating_std, df_award_count]
    df_grouped = reduce(lambda left, right: pd.merge(left, right, on=group_by_cols), df_singles)
    df_grouped['award_winning_share'] = df_grouped['award_winning_count'] / df_grouped['book_count']

    return df_grouped


def optimal_dt_accuracy(X_train, y_train, X_test, y_test, max_depth_list):
    '''
    INPUT:
    X_train - training dataframe holding all features (after dummy encoding)
    y_train - training series holding the labels
    X_test - test dataframe holding all features (after dummy encoding)
    y_test - test series holding the labels
    max_depth_list - a list holding all max_depth values the decision tree should be optimized on

    OUTPUT:
    Plot of train and test accuracy for all max_depth values.

    THE FUNCTION plots train and test accuracy in order to find the optimal max_depth parameter.
    '''
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import tree
    from sklearn.metrics import accuracy_score

    train_accuracy = []
    test_accuracy = []

    for x in max_depth_list:
        clf = tree.DecisionTreeClassifier(max_depth=x)
        clf.fit(X_train, y_train)

        pred_y_train = clf.predict(X_train)
        pred_y_test = clf.predict(X_test)

        train_accuracy.append(accuracy_score(y_train, pred_y_train))
        test_accuracy.append(accuracy_score(y_test, pred_y_test))
        print('Accuracy with maximum depth {} computed.'.format(str(x)))

    x = np.arange(len(max_depth_list)) + 1

    fig, ax = plt.subplots(figsize=(16, 8))
    plt.plot(x, train_accuracy, color='indianred', label='Train Accuracy')
    plt.plot(x, test_accuracy, color='steelblue', label='Test Accuracy')
    plt.xlabel('Maximum Depth')
    plt.ylabel('Accuracy')
    plt.xticks(np.arange(1, 5.5, 1))
    yticks = ax.get_yticks()
    ax.set_yticks(yticks)
    ax.set_yticklabels(['{:,.0%}'.format(y) for y in yticks])
    plt.legend(loc='upper right')
    plt.show()
